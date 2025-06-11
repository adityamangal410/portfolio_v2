import os, re
from typing import List

def parse_front_matter(path):
    yaml = {}
    with open(path, encoding='utf-8') as fh:
        lines = fh.readlines()
    if not lines or lines[0].strip() != '---':
        return yaml, lines
    i = 1
    front = ['---\n']
    while i < len(lines):
        line = lines[i]
        i += 1
        if line.strip() == '---':
            front.append('---\n')
            break
        front.append(line)
    else:
        return yaml, lines
    # parse yaml simple
    i = 1
    while i < len(front)-1:
        line = front[i]
        if ':' in line:
            key, val = line.split(':', 1)
            key = key.strip()
            val = val.strip()
            if val == '':
                values: List[str] = []
                i += 1
                while i < len(front)-1 and front[i].startswith('  -'):
                    values.append(front[i].strip()[2:].strip())
                    i += 1
                yaml[key] = values
                continue
            yaml[key] = val.strip('"').strip("'")
        i += 1
    return yaml, lines

def update_file(path):
    yaml, lines = parse_front_matter(path)
    output_file = yaml.get('output-file')
    if output_file:
        slug = os.path.splitext(output_file)[0]
    else:
        slug = yaml.get('slug')
        if not slug:
            slug = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', os.path.splitext(os.path.basename(path))[0])
        output_file = f'{slug}.html'
    if yaml.get('output-file') == output_file and 'slug' not in yaml:
        return False
    # insert or replace output-file
    new_lines = []
    in_yaml = False
    updated = False
    i = 0
    if lines and lines[0].strip() == '---':
        new_lines.append(lines[0])
        in_yaml = True
        i = 1
        while i < len(lines):
            line = lines[i]
            i += 1
            if line.strip() == '---':
                if not updated:
                    new_lines.append(f'output-file: {output_file}\n')
                    updated = True
                new_lines.append(line)
                break
            if line.startswith('output-file:'):
                if not updated:
                    new_lines.append(f'output-file: {output_file}\n')
                    updated = True
                continue
            if line.startswith('slug:'):
                # drop legacy slug field
                continue
            new_lines.append(line)
        new_lines.extend(lines[i:])
    else:
        return False
    with open(path, 'w', encoding='utf-8') as fh:
        fh.writelines(new_lines)
    return True


def main():
    changed = False
    for f in os.listdir('posts'):
        if not f.endswith('.qmd') or f == 'index.qmd':
            continue
        path = os.path.join('posts', f)
        if update_file(path):
            print('updated', path)
            changed = True
    if not changed:
        print('no updates')

if __name__ == '__main__':
    main()
