# Rishub Tamirisa's website

A small, theme-free Hugo site. The original Signifier typography, layout, news
scroller, and compact research cards with visuals on the right are retained without PaperMod, Sass,
Node packages, or a client-side framework.

## Preview locally

Install [Hugo](https://gohugo.io/installation/) (the deployment uses **0.123.7**), then:

```sh
hugo server --baseURL http://localhost:1313/
```

Open http://localhost:1313/. Hugo reloads the preview as files change.

## Edit content

- `data/profile.json`: biography, portrait, and social links.
- `data/news.json`: news in display order. Each item has a date and text.
- `data/research.json`: selected research in display order. Copy an entry to add
  work; specify the title, authors, venue and a list of links (`label`, `url`, and `icon`), image, and descriptive
  alt text. Optional `preview_url` links the visual to a blog; paper visuals link to the full figure. Full author lists are always visible in slightly smaller type. Optional `description` adds a concise explanation below the authors.
- `static/images/research/`: new preview figures. Paths in the data are relative
  to the site root, so both project URLs and custom domains work.
- `content/papers/`: existing paper pages and their downloads, with URLs preserved.
- `static/css/site.css`: all typography, spacing, responsive rules, and colors.
- `layouts/index.html` and `layouts/partials/research-card.html`: homepage and
  shared research markup. Other layouts support the existing secondary pages.

Content fields that need inline emphasis/links accept trusted HTML. The biography
accepts Markdown. Keep content edits in the data files, not in the templates.
The homepage works without JavaScript; the only script adds citation-copy buttons
on paper pages. Fonts are local and have a single source in `static/fonts/`.

## Build and deploy

```sh
hugo --minify --cleanDestinationDir
python3 scripts/check_site.py public
```

One GitHub Actions workflow (`.github/workflows/pages.yml`) builds and validates
pull requests. Pushes to `main` and manual runs also deploy to GitHub Pages using
the existing Pages environment. Pages must use **GitHub Actions** as its source.
There is no Sass installation, npm install, theme checkout, or submodule setup.
The production base URL is configured in `config.yml`; deployment uses the URL
provided by GitHub Pages, including a custom domain if one is configured.

## Preview figure sources

Blog artwork fills the right-hand column; paper figures fit completely inside it with a small white margin. Images do not increase the text height. The Intology cards use the same artistic banners as the original blogs:

- [NanoGPT-Bench banner](https://intology.ai/brand/visual/blog-1-roots.jpg)
  — [blog](https://intology.ai/blog/nanogpt-bench), May 19, 2026.
- [Scaling Automated Post-Training banner](https://intology.ai/brand/visual/blog-4-spheres.jpg)
  — [blog](https://intology.ai/blog/scaling-automated-post-training), August 3, 2026.

Earlier papers use their complete, uncropped original figures. Click a paper's visual to see the full,
uncropped image. Banner sources are recorded in the corresponding research data.
Existing assets and the original design's MIT attribution remain in `LICENSE.md`.

The arXiv and Substack SVG marks come from [Simple Icons](https://github.com/simple-icons/simple-icons) (CC0); GitHub and Twitter marks are retained from the original site. Other resource icons are small inline SVGs.

Resource logos: [X via Simple Icons](https://github.com/simple-icons/simple-icons/blob/develop/icons/x.svg), [WIRED official wordmark](https://www.wired.com/verso/static/wired-us/assets/logo.svg), and [Intology official dark symbol](https://intology.ai/brand/logo/mark-dark.svg).

The TIME wordmark is the official inline SVG from [time.com](https://time.com/). WIRED and TIME wordmarks are used as the link labels, with an underline and inherited hover color.
