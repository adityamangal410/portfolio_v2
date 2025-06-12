import glob, os, re, subprocess, sys

QUARTO = '/tmp/quarto/bin/quarto'

for path in sorted(glob.glob('posts/*.qmd')):
    if os.path.basename(path) == 'index.qmd':
        continue
    with open(path, encoding='utf-8') as f:
        text = f.read()
    m = re.match(r'---\n.*?---\n', text, flags=re.S)
    if m:
        front = m.group(0)
        body = text[m.end():]
    else:
        front = ''
        body = text
    # Convert markdown -> html -> markdown to strip html tags
    p1 = subprocess.run([QUARTO, 'pandoc', '-', '-f', 'markdown', '-t', 'html'],
                        input=body, text=True, capture_output=True)
    html = p1.stdout
    p2 = subprocess.run([QUARTO, 'pandoc', '-', '-f', 'html', '-t', 'gfm', '--markdown-headings=atx'],
                        input=html, text=True, capture_output=True)
    md = p2.stdout
    with open(path, 'w', encoding='utf-8') as f:
        f.write(front + md)
    print('processed', path)
