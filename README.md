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


### Installing and running Jekyll (how-to run the website locally)

**1. Install Jekyll and dependencies.** First thing you're going to need to do is set up
Jekyll and the appropriate dependencies so you can develop locally. The easiest way to
install everything is to use [RubyGems](https://rubygems.org/pages/download) and follow
the instructions on the [Jekyll](http://jekyllrb.com/docs/installation/) website. In addition
to the basic Jekyll installation, you also need to install a few dependency gems.
After installing RubyGems on your machine, you really only need to run one basic command:

`gem install jekyll`


On Ubuntu, run:
```bash
sudo apt install ruby ruby-dev make gcc
sudo gem install jekyll bundler
sudo gem install jekyll-seo-tag
sudo gem install jekyll-sitemap
```

**2. Run a local version of the website.** Using Git, clone the latest version of this repository
to your local machine using the following command:

`git clone https://github.com/triplea-game/triplea-game.github.io.git`

Then start the jekyll server:

```
cd triplea-game.github.io/
jekyll serve`
```

This will get a local version of the website running on your machine, accessible
on `localhost:4000`, or whatever the terminal tells you. 

**3. Make Changes**

You can then make changes to the files you cloned earlier and the local server
should update automatically. You can then preview any changes on your local machine
with a web browser, just refresh the page `localhost:4000`.

** Tip:** Write any content in [Markdown](https://daringfireball.net/projects/markdown/)
with the [YAML front matter](http://jekyllrb.com/docs/frontmatter/) like the other pages.
If you can, follow the instructions below to test your changes.

**3. Commit and submit pull request**

After verifying changes to your locally cloned repository, you'll need a git client of
some sort installed (there are many of these, [git for windows](https://gitforwindows.org/) is an example).
Follow these steps to prepare a pull-request: 
<https://github.com/PointCloudLibrary/pcl/wiki/A-step-by-step-guide-on-preparing-and-submitting-a-pull-request>

