# https://adityamangal.com

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/adityamangal410/portfolio_v2/binder?urlpath=rstudio)
[![Netlify Status](https://api.netlify.com/api/v1/badges/43286211-047d-417f-b96d-680530d38597/deploy-status)](https://app.netlify.com/sites/upbeat-knuth-c15bbd/deploys)

Hello visitor!

This is the github repo to my blog / portfolio that you can check out here - [Aditya Mangal Portfolio](https://www.adityamangal.com/)

You can get most of the information about me on the blog. Some more things about me here -   

1. I work in the Location Center of Excellence at Yahoo. 
2. I'm originally from India, currently living in the San Francisco Bay Area since past few years. 
3. I like to blog about technical stuff mostly related to Data Science and Machine Learning. 
4. Java is my first love and R/Python are competing for a close second. 
4. In an ideal world, this blog would also contain my writings about travel, random musings and photography among other things. One day, some day. 
5. If you have any questions or suggestions or feedback, you're always welcome to connect with me at adityamangal410 [at] yahoo [dot] co [dot] in.

Here are the technologies/tools and their references that I'm mostly using to run this blog -

- [Quarto](https://quarto.org/) - Static site generator with Markdown and Jupyter notebook support.
- [Netlify](https://www.netlify.com/) - For CD and DNS.
- [RStudio](https://www.rstudio.com/) or any text editor - For development and testing.
- [Unsplash](https://unsplash.com/) - For article cover images.
- [Distill theme](https://distill.pub) via Quarto - Blog theme.
Legacy posts live under the `post/` folder but are also converted to Quarto
files using `tools/convert_posts.py`. The generated `.qmd` files in `posts/`
apply the Distill theme so the articles look consistent with the rest of the
site. Old URLs like `/post/my-post.html` redirect to the new pages via Netlify.

To regenerate the converted posts after editing the HTML originals, run
`python tools/convert_posts.py` and then `quarto render`.

## Authoring new blog posts

The `posts/` folder contains the Quarto sources for all articles. You can write
posts in several formats and Quarto will convert them to HTML when you run
`quarto render`.

### Jupyter Notebook (`.ipynb`)

1. Create a new notebook under `posts/` with a descriptive name, e.g.
   `my-post.ipynb`.
2. Add a Markdown cell at the top containing the YAML front matter wrapped in
   `---` fences. Include at least a `title` and `date` field.
3. Write your content in subsequent cells and execute them as usual.
4. Run `quarto render` to build the site and preview the generated HTML page.

### Markdown (`.md`)

1. Create `my-post.md` in the `posts/` directory.
2. Start the file with a YAML header between `---` lines specifying metadata
   like `title`, `author` and `date`.
3. Write the article in Markdown and render the site with `quarto render`.

### R Markdown (`.Rmd`)

1. Place a new `.Rmd` file inside `posts/`.
2. Define the YAML front matter at the top and write your R Markdown content
   below it. Code chunks will be executed during rendering.
3. Build the site with `quarto render` to produce the HTML post.

### Quarto document (`.qmd`)

1. For most posts you can create a `.qmd` file such as `my-post.qmd` in
   `posts/`.
2. Add the YAML header followed by your Markdown and code chunks.
3. Run `quarto render` to generate the final page.

## Testing pull requests

Follow these steps to review changes locally before merging:

1. **Install Quarto** by downloading it from [quarto.org](https://quarto.org/docs/get-started/).
2. Install Python packages used for rendering with `pip install ipykernel pyyaml nbformat nbclient`.
3. Clone the repository and check out the pull request branch.
4. Run `quarto render` to build the site and ensure it compiles without errors.
5. Preview the result with `quarto preview` and browse to `http://localhost:4200`.
6. Verify that the GitHub Actions workflow passes on the pull request page.

These steps confirm that both the local build and the CI workflow are functioning correctly.
