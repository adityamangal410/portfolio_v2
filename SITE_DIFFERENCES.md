# Site Diff Results

The `compare_sites.py` script was executed with:

```bash
python tools/compare_sites.py -q https://www.adityamangal.com \
  https://deploy-preview-31--upbeat-knuth-c15bbd.netlify.app
```

## Differences Found

- `index.html` differed between the two sites
- Directories present only in the Netlify site:
  - `.netlify`
  - `about`
  - `post`
  - `posts`
  - `robots.txt`
  - `site_libs`
  - `static`

A total of 193 link differences were ignored due to domain rewrites.

See `site_diff.patch` for the complete diff output.
