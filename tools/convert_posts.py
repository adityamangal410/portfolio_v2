import os, glob

posts_dir = 'post'
output_dir = 'posts'
os.makedirs(output_dir, exist_ok=True)

for html_path in glob.glob(os.path.join(posts_dir, '*.html')):
    slug = os.path.splitext(os.path.basename(html_path))[0]
    qmd_path = os.path.join(output_dir, f"{slug}.qmd")
    with open(html_path, encoding='utf-8') as f:
        lines = f.readlines()
    body_start = 0
    yaml_lines = []
    if lines and lines[0].strip() == '---':
        for i in range(1, len(lines)):
            if lines[i].strip() == '---':
                body_start = i + 1
                yaml_lines = lines[1:i]
                break
    body = ''.join(lines[body_start:])
    normalized_yaml = []
    skip_keys = {'comments', 'showMeta', 'showActions'}
    for line in yaml_lines:
        key = line.split(':',1)[0].strip()
        if key in skip_keys:
            continue
        if line.strip().endswith(': no'):
            normalized_yaml.append(line.replace(': no', ': false'))
        elif line.strip().endswith(': yes'):
            normalized_yaml.append(line.replace(': yes', ': true'))
        else:
            normalized_yaml.append(line)
    with open(qmd_path, 'w', encoding='utf-8') as out:
        out.write('---\n')
        out.writelines(normalized_yaml)
        out.write('format:\n  html:\n    theme: distill\nfreeze: true\n')
        out.write('---\n\n')
        out.write(body)
print('Converted', len(glob.glob(os.path.join(posts_dir, '*.html'))), 'posts')
