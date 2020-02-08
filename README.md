[![Travis](https://img.shields.io/travis/triplea-game/triplea-game.github.io.svg?style=flat-square)](https://travis-ci.org/triplea-game/triplea-game.github.io)
# [TripleA Website](http://triplea-game.github.io/)

This is the official TripleA website. This repository hosts the website source code. The TripleA site runs on [Jekyll](http://jekyllrb.com/) and [GitHub Pages](https://pages.github.com/). Pages are written in [markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).


## A Guide on How-To-Contribute

This is a guide for contribution to the website. For now, please start all feature requests as issues. Please note that we will often hesitate to accept pull requests without prior approval, but it is very easy to start an issue first, so that we can help you fit your idea into the project.



## Making code changes

If you are interested in making changes to the design, functionality, or structure of the blog, you're going to need to set up a local environment and understand some of the technologies behind the site.

**1. Install Jekyll and dependencies.** First thing you're going to need to do is set up Jekyll and the appropriate dependencies so you can develop locally. The easiest way to install everything is to use [RubyGems](https://rubygems.org/pages/download) and follow the instructions on the [Jekyll](http://jekyllrb.com/docs/installation/) website. In addition to the basic Jekyll installation, you also need to install a few dependency gems. After installing RubyGems on your machine, you really only need to run one basic command:

`gem install jekyll`


Ubuntu:
```bash
sudo apt install ruby ruby-dev make gcc
sudo gem install jekyll bundler
```

**2. Run a local version of the blog.** Using Git, clone the latest version of this repository to your local machine using the following command:

`git clone https://github.com/triplea-game/triplea-game.github.io.git`

Then go into root of the folder and run `jekyll serve`:

`cd triplea-game.github.io && jekyll serve`

This will get a local version of the blog running on your machine, accessible on `localhost:4000, or whatever the terminal tells you`

**3. Read up on the documentation.** To really understand how to develop the site there are a few things you're going to need to read up on to make meaningful changes:

- [Jekyll](http://jekyllrb.com/docs/home/) The static site generator used for the site
- [GitHub Pages](https://help.github.com/articles/using-jekyll-with-pages/) How the site is hosted
- [Liquid](https://help.shopify.com/themes/liquid/basics) The templating language used with Jekyll by Shopify


** Tip:** Write any content in [Markdown](https://daringfireball.net/projects/markdown/) with the [YAML front matter](http://jekyllrb.com/docs/frontmatter/) like the other pages. If you can, follow the instructions below to test your changes.


## Image Storage and Git LFS

Images and binary files should be tracked and checked in using 'git-lfs': https://git-lfs.github.com/

