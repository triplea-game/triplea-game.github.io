# [TripleA Website](http://triplea-game.github.io/)

## Getting Started
The TripleA site runs on [Jekyll](http://jekyllrb.com/) and [GitHub Pages](https://pages.github.com/). Pages are written in [markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).

This is a guide for contribution to the website. For now, please start all feature requests as issues and send pull requests to William DeKryger's ([The Red Baron](http://tripleadev.1671093.n2.nabble.com/template/NamlServlet.jtp?macro=user_nodes&user=396161)) [repo](https://github.com/williamdekryger/triplea-game.github.io), as that is where the latest version will alway be.

## About the site
This is the official TripleA website, which is in early development. Please contact William DeKryger or start an issue if you want to help out/have a request. There are a few places where you can go to discuss the site:

* [Thread for General Discussion About the Site on the Dev forum](http://tripleadev.1671093.n2.nabble.com/TripleA-Website-Redesign-Migration-to-Github-Pages-tp7589306p7589426.html)
* [Thread for volunteering to help out](http://tripleadev.1671093.n2.nabble.com/TripleA-Website-Development-tp7589352p7589383.html)
* [Issues page on the Red Baron's repo](https://github.com/williamdekryger/triplea-game.github.io/issues)

## I have an idea for / want to write a page, what should I do?
1. Bring it up in an issue or email William DeKryger [via the forum](http://tripleadev.1671093.n2.nabble.com/template/NamlServlet.jtp?macro=user_nodes&user=396161). He will probably get back to you within a few days.
2. Write any content in Markdown with the [YAML front matter](http://jekyllrb.com/docs/frontmatter/) like the others. If you can, follow the instructions below to test your changes.
3. He will direct you what to do, but if you want to quickly shoot him your changes, send a pull request to [his repo](https://github.com/williamdekryger/triplea-game.github.io), where the latest changes are. (This is until the site leaves development.)

## Making code changes

If you are interested in making changes to the design, functionality, or structure of the blog, you're going to need to set up a local environment and understand some of the technologies behind the site.

**1. Install Jekyll and dependencies.** First thing you're going to need to do is set up Jekyll and the appropriate dependencies so you can develop locally. The easiest way to install everything is to use [RubyGems](https://rubygems.org/pages/download) and follow the instructions on the [Jekyll](http://jekyllrb.com/docs/installation/) website. In addition to the basic Jekyll installation, you also need to install a few dependency gems. After install RubyGems on your machine, you really only to run two basic commands:
```
gem install jekyll
gem install jekyll-sitemap
gem install jekyll-redirect-from
gem install rouge
```

**2. Run a local version of the blog.** Using Git, clone the latest version of this repository to your local machine using the following command:

`git clone https://github.com/triplea-game/triplea-game.github.io.git`

Then go into root of the folder and run `jekyll serve`:

`cd triplea-game.github.io`

`jekyll serve`

This will get a local version of the blog running on your machine, accessible on `localhost:4000/blog/`

**3. Read up on the documentation.** To really understand how to develop the site there are a few things you're going to need to read up on to make meaningful changes:
 - [Jekyll](http://jekyllrb.com/docs/home/) The static site generator used for the site
 - [GitHub Pages](https://help.github.com/articles/using-jekyll-with-pages/) How the site is hosted
 - [Liquid](https://docs.shopify.com/themes/liquid-documentation/basics) The templating language used with Jekyll by Shopify
