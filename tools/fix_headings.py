import sys, re, os

for path in sys.argv[1:]:
    with open(path) as f:
        lines = f.read().splitlines()

    stack = []
    out_lines = []
    skip_toc = False
    for line in lines:
        stripped = line.strip()
        if skip_toc:
            if stripped == '</div>':
                skip_toc = False
            continue
        if stripped == '<div id="TOC">':
            skip_toc = True
            continue
        if re.match(r'<div id=".*" class="section level[0-9]">', stripped):
            stack.append('section')
            continue
        m = re.match(r'<h([1-6])>(.*)</h\1>', stripped)
        if m:
            level = int(m.group(1))
            text = m.group(2)
            out_lines.append('#'*level + ' ' + text)
            continue
        if stripped == '</div>' and stack:
            stack.pop()
            continue
        out_lines.append(line)
    with open(path, 'w') as f:
        f.write('\n'.join(out_lines) + '\n')
