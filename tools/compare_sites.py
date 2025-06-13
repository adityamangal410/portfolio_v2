#!/usr/bin/env python3
"""Download two sites and diff them while ignoring domain differences."""
import argparse
import os
import re
import shutil
import subprocess
import tempfile


def run(cmd, check=False, allow=None):
    """Run *cmd* and optionally validate exit codes."""
    res = subprocess.run(cmd, text=True)
    if res.returncode != 0:
        print(f"Command {' '.join(cmd)} exited with code {res.returncode}")
    if check:
        allowed = {0} if allow is None else set(allow)
        if res.returncode not in allowed:
            raise subprocess.CalledProcessError(res.returncode, cmd)
    return res.returncode


def download(url, out_dir):
    """Mirror *url* into *out_dir* using wget."""
    # Wget may return a non-zero code for missing pages. We ignore
    # those so the comparison can continue even if some assets fail.
    run(["wget", "-mk", "-nH", url, "-P", out_dir], allow=range(0, 9))


def sanitize(directory):
    count = 0
    for root, _, files in os.walk(directory):
        for name in files:
            if name.lower().endswith((".html", ".htm", ".xml", ".js", ".css")):
                path = os.path.join(root, name)
                with open(path, "r", encoding="utf-8", errors="ignore") as fh:
                    data = fh.read()
                cleaned, n = re.subn(r"https?://[^\s'\"]+", "URL", data)
                if n:
                    count += n
                    with open(path, "w", encoding="utf-8") as fh:
                        fh.write(cleaned)
    return count


def main():
    p = argparse.ArgumentParser(
        description="Mirror two sites and diff them, ignoring link domains"
    )
    p.add_argument("site1", help="Base site URL")
    p.add_argument("site2", help="Comparison site URL")
    args = p.parse_args()

    dirs = [tempfile.mkdtemp(), tempfile.mkdtemp()]
    try:
        download(args.site1, dirs[0])
        download(args.site2, dirs[1])
        link_diff = sanitize(dirs[0]) + sanitize(dirs[1])
        run(["diff", "-r", dirs[0], dirs[1]], check=True, allow={0,1})
        if link_diff:
            print(f"Ignored {link_diff} URL link differences due to domain changes")
    finally:
        for d in dirs:
            shutil.rmtree(d)


if __name__ == "__main__":
    main()
