import glob, os, re

for path in sorted(glob.glob('posts/*.qmd')):
    if os.path.basename(path) == 'index.qmd':
        continue
    with open(path, encoding='utf-8') as f:
        lines = f.read().splitlines()

    out_lines = []
    in_code = False
    for line in lines:
        if line.strip().startswith('```'):
            in_code = not in_code
            out_lines.append(line.rstrip())
            continue
        if in_code:
            out_lines.append(line.rstrip())
            continue
        # drop script/style/link tags entirely
        if re.search(r'<(script|style|link)[^>]*>', line):
            continue
        # convert anchor tags with any attributes to markdown links
        line = re.sub(r'<a\s+href="([^"]+)"[^>]*>(.*?)</a>', r'[\2](\1)', line)
        line = line.replace('<p>', '').replace('</p>', '')
        line = re.sub(r'<li><p>(.*?)</p></li>', r'- \1', line)
        line = re.sub(r'<li>(.*?)</li>', r'- \1', line)
        line = line.replace('<li>', '- ').replace('</li>', '')
        line = re.sub(r'</?(ul|ol)[^>]*>', '', line)
        line = re.sub(r'<strong>(.*?)</strong>', r'**\1**', line)
        line = re.sub(r'<em>(.*?)</em>', r'*\1*', line)
        line = re.sub(r'<br\s*/?>', '  ', line)
        line = re.sub(r'</?(div|span)[^>]*>', '', line)
        out_lines.append(line.rstrip())

    cleaned = []
    prev_blank = False
    for l in out_lines:
        if l.strip() == '':
            if not prev_blank:
                cleaned.append('')
            prev_blank = True
        else:
            cleaned.append(l)
            prev_blank = False

    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(cleaned) + '\n')
    print('cleaned', path)
