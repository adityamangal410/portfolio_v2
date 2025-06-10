import os, glob, re
from typing import List

TEMPLATE = r"""---
title: "Category: {cat}"
jupyter: python3
execute:
  echo: false
---

```{{python}}
CATEGORY = "{cat}"

import glob, os, re
from typing import List
from html import escape
from IPython.display import HTML, display


def parse_front_matter(path):
    yaml = {{}}
    with open(path, encoding='utf-8') as fh:
        lines = fh.readlines()
    if not lines or lines[0].strip() != '---':
        return yaml
    i = 1
    while i < len(lines):
        line = lines[i]
        i += 1
        if line.strip() == '---':
            break
        if ':' in line:
            key, val = line.split(':', 1)
            key = key.strip()
            val = val.strip()
            if val == '':
                values: List[str] = []
                while i < len(lines) and lines[i].startswith('  -'):
                    values.append(lines[i].strip()[2:].strip())
                    i += 1
                yaml[key] = values
            else:
                yaml[key] = val.strip('"').strip("'")
    return yaml


def extract_first_local_image(path):
    with open(path, encoding='utf-8') as fh:
        text = fh.read()
    if text.startswith('---'):
        parts = text.split('---', 2)
        if len(parts) == 3:
            text = parts[2]
    for m in re.finditer(r'<img[^>]+src=\"([^\"]+)\"', text):
        src = m.group(1)
        if not src.startswith('http://') and not src.startswith('https://'):
            return src
    for m in re.finditer(r'!\\[[^\\]]*\\]\\(([^)]+)\\)', text):
        src = m.group(1)
        if not src.startswith('http://') and not src.startswith('https://'):
            return src
    return None

posts = []
for f in glob.glob('../posts/*.qmd'):
    if os.path.basename(f) == 'index.qmd':
        continue
    meta = parse_front_matter(f)
    cats = meta.get('categories', [])
    if isinstance(cats, str):
        cats = [cats]
    if CATEGORY not in cats:
        continue
    slug = os.path.splitext(os.path.basename(f))[0]
    url = f'../posts/{{slug}}.html'
    image = extract_first_local_image(f)
    if not image:
        image = meta.get('coverImage') or meta.get('thumbnailImage', '')
    posts.append(
        (
            meta.get('date', ''),
            cats,
            meta.get('title', slug),
            meta.get('summary', ''),
            url,
            image,
        )
    )

posts.sort(reverse=True)

blocks = []
for date, cats, title, summary, url, image in posts:
    img_tag = f'<img src="{{escape(image)}}" alt="{{escape(title)}}">' if image else ''
    if isinstance(cats, list):
        cat_links = []
        for cat in cats:
            slug = cat.lower().replace(' ', '-')
            cat_links.append(f'<a class="cat-link" href="{{escape(slug)}}.html">{{escape(cat)}}</a>')
        cats_str = ' '.join(cat_links)
    elif cats:
        slug = cats.lower().replace(' ', '-')
        cats_str = f'<a class="cat-link" href="{{escape(slug)}}.html">{{escape(cats)}}</a>'
    else:
        cats_str = ''
    blocks.append(
        f'''<div class="post-block">\n  <div class="post-meta">\n    <div class="post-date">{{escape(date)}}</div>\n    <div class="post-cats">{{cats_str}}</div>\n  </div>\n  <div class="post-info">\n    <h2><a href="{{escape(url)}}">{{escape(title)}}</a></h2>\n    <p>{{escape(summary)}}</p>\n  </div>\n  {{img_tag}}\n</div>'''
    )

display(HTML('\n'.join(blocks)))
```
"""

def parse_post_front_matter(path):
    yaml = {}
    with open(path, encoding='utf-8') as fh:
        lines = fh.readlines()
    if not lines or lines[0].strip() != '---':
        return yaml
    i = 1
    while i < len(lines):
        line = lines[i]
        i += 1
        if line.strip() == '---':
            break
        if ':' in line:
            key, val = line.split(':', 1)
            key = key.strip()
            val = val.strip()
            if val == '':
                values = []
                while i < len(lines) and lines[i].startswith('  -'):
                    values.append(lines[i].strip()[2:].strip())
                    i += 1
                yaml[key] = values
            else:
                yaml[key] = val.strip('"').strip("'")
    return yaml


def main():
    categories = set()
    os.makedirs('categories', exist_ok=True)
    for f in glob.glob('posts/*.qmd'):
        if os.path.basename(f) == 'index.qmd':
            continue
        meta = parse_post_front_matter(f)
        cats = meta.get('categories', [])
        if isinstance(cats, str):
            cats = [cats]
        for cat in cats:
            categories.add(cat)

    for cat in sorted(categories):
        slug = cat.lower().replace(' ', '-')
        out_path = os.path.join('categories', f'{slug}.qmd')
        with open(out_path, 'w', encoding='utf-8') as out:
            out.write(TEMPLATE.format(cat=cat))

if __name__ == '__main__':
    main()
