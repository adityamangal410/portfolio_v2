import glob
import os
import re

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
            out_lines.append(line)
            continue
        if in_code:
            out_lines.append(line)
        else:
            line = re.sub(r'<li><p>(.*?)</p></li>', r'- \1', line)
            line = re.sub(r'<li>(.*?)</li>', r'- \1', line)
            line = re.sub(r'</?(ul|ol)[^>]*>', '', line)
            line = re.sub(r'<p>(.*?)</p>', r'\1', line)
            line = re.sub(r'</?[^>]+>', '', line)
            out_lines.append(line)
    # collapse multiple blank lines
    cleaned = []
    prev_blank = False
    for l in out_lines:
        if l.strip() == '':
            if not prev_blank:
                cleaned.append('')
            prev_blank = True
        else:
            cleaned.append(l.rstrip())
            prev_blank = False
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(cleaned) + '\n')
    print('processed', path)
