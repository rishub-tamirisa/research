// The only client-side enhancement: copy citations on existing paper pages.
if (navigator.clipboard) {
  document.querySelectorAll('pre > code').forEach((code) => {
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'copy-code';
    button.textContent = 'copy';
    button.addEventListener('click', async () => {
      try {
        await navigator.clipboard.writeText(code.textContent);
        button.textContent = 'copied!';
      } catch {
        button.textContent = 'Select text to copy';
      }
      setTimeout(() => { button.textContent = 'copy'; }, 2000);
    });
    code.parentElement.before(button);
  });
}
