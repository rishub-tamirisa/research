#!/usr/bin/env python3
"""Check a Hugo build's local links, assets, document structure, and research data.

Usage: python3 scripts/check_site.py [output-directory]
Works with root domains and GitHub Pages project prefixes. No dependencies.
"""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import json
import re
import sys


class Document(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.tags = Counter()
        self.refs = []
        self.canonical = None
        self.research_cards = 0
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags[tag] += 1
        if tag == 'article' and 'research-card' in attrs.get('class', '').split():
            self.research_cards += 1
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonical = attrs['href']
        if tag in ('a', 'link') and 'href' in attrs:
            self.refs.append(attrs['href'])
        if tag in ('img', 'script') and 'src' in attrs:
            self.refs.append(attrs['src'])


def check(output):
    home = Document((output / 'index.html').read_text())
    assert home.canonical, 'Homepage needs a canonical URL'
    base = urlsplit(home.canonical)
    prefix = base.path.rstrip('/') + '/'
    errors = []

    def local_target(ref, current):
        url = urlsplit(urljoin(current, ref))
        if url.scheme not in ('http', 'https') or url.netloc != base.netloc:
            return
        if not url.path.startswith(prefix):
            errors.append(f'Local URL escapes site prefix: {url.path}')
            return
        target = output / unquote(url.path[len(prefix):])
        if target.is_dir():
            target /= 'index.html'
        if not target.is_file():
            errors.append(f'Missing local target: {url.path}')

    pages = list(output.rglob('*.html'))
    for path in pages:
        doc = Document(path.read_text())
        for tag in ('html', 'head', 'body', 'main', 'title'):
            if doc.tags[tag] != 1:
                errors.append(f'{path}: expected one {tag}, found {doc.tags[tag]}')
        current = urljoin(home.canonical, path.relative_to(output).as_posix())
        for ref in doc.refs:
            local_target(ref, current)
    for path in output.rglob('*.css'):
        current = urljoin(home.canonical, path.relative_to(output).as_posix())
        for ref in re.findall(r'url\([\'\"]?([^\)\'\"]+)', path.read_text()):
            local_target(ref, current)
    root = Path(__file__).resolve().parents[1]
    research = json.loads((root / 'data/research.json').read_text())
    assert home.research_cards == len(research), 'Research cards missing from homepage'
    for item in research:
        for key in ('title', 'authors', 'venue', 'links', 'image', 'alt'):
            assert item.get(key), f'Research entry missing {key}: {item}'
        assert (output / item['image']).is_file(), f'Missing preview: {item["image"]}'
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'Checked {len(pages)} pages, {len(research)} research cards, and all local links/assets.')


if __name__ == '__main__':
    check(Path(sys.argv[1] if len(sys.argv) > 1 else 'public').resolve())
