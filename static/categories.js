// Convert category labels to links
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.quarto-category').forEach(el => {
    const text = el.textContent.trim();
    if (!text) return;
    const slug = text.toLowerCase().replace(/\s+/g, '-');
    const link = document.createElement('a');
    link.textContent = text;
    link.href = `../categories/${slug}.html`;
    link.className = 'quarto-category cat-link';
    el.replaceWith(link);
  });
});
