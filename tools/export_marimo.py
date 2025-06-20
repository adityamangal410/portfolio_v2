import glob
import os
import subprocess

for path in glob.glob('posts/*.py'):
    out_path = os.path.splitext(path)[0] + '.qmd'
    subprocess.run(['marimo', 'export', 'md', path, '-o', out_path], check=True)
    print(f"Converted {path} -> {out_path}")
