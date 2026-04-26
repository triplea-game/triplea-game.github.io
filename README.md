# [TripleA Website](httpis://triplea-game.github.io/)

This repository hosts the markdown source code for the triplea website: <https://triplea-game.github.io>

Updates to this repository (master branch) will update the website in close to real time.


The TripleA site runs on [Jekyll](http://jekyllrb.com/) 
and [GitHub Pages](https://pages.github.com/). 

Pages are written in [markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).


## How-To-Contribute 

We may hesitate to accept pull requests without prior discussion, but it is very easy
to start a [discussion thread](https://github.com/triplea-game/triplea-game.github.io/discussions)
first so that we can help you fit your idea into the project.

If there is no response from the discussion thread, try posting in the [forums](https://forums.triplea-game.org/)

Write permissions are granted to those who have a small track record of solid updates and who would like
to do more than just a few changes here and there.

## Merge Policy

For those with write privileges, merge policy is - "Ship, show, ask": <https://martinfowler.com/articles/ship-show-ask.html>

## Making Website Change

You can edit any page individually by navigating to the page in
github and using the github 'pencil icon': 
<https://www.freecodecamp.org/news/how-to-make-your-first-pull-request-on-github/>

For more involved changes, you'll want to preview those changes
locally before creating a pull request.  The TripleA website is
run on Jekyll, hosted by Github Pages. Jekyll is an engine that
serves markdown (md) files as HTML, once running it'll compile
and host the website on your local computer (usually at http://localhost:4000).

For more detailed information, see:
- <https://help.github.com/en/github/working-with-github-pages/about-github-pages-and-jekyll>
- <https://help.github.com/en/github/working-with-github-pages/testing-your-github-pages-site-locally-with-jekyll>
- <https://help.github.com/articles/using-jekyll-with-pages/>
- <http://jekyllrb.com/docs/home/> - The static site generator used for the site


### Local Dev Setup

```bash
git clone https://github.com/triplea-game/triplea-game.github.io.git
cd triplea-game.github.io/

make install-jekyll   # installs Ruby, Bundler, and all gems pinned in Gemfile.lock (Ubuntu/Debian)
make setup            # installs pre-commit and registers the git push hook
make serve            # starts the site at http://localhost:4000
```

The server reloads automatically when you save changes. Preview your edits in a browser at `localhost:4000`.

Write content in [Markdown](https://daringfireball.net/projects/markdown/) with
[YAML front matter](http://jekyllrb.com/docs/frontmatter/) like the other pages.

Run `make` with no arguments to see all available commands.

**Submitting a pull request**

After verifying changes locally, follow these steps to prepare a pull request:
<https://github.com/PointCloudLibrary/pcl/wiki/A-step-by-step-guide-on-preparing-and-submitting-a-pull-request>

