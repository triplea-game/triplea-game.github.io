# TripleA Website — Copilot Instructions

## Project
Static site for [triplea-game.github.io](https://triplea-game.github.io).
Built with **Jekyll** (kramdown, SASS), hosted on **GitHub Pages**.

## Key Directories
- `site/` — Jekyll source; only this directory is published
- `site/_layouts/`, `site/_includes/` — Jekyll templates (HTML)
- `site/_sass/` — stylesheets
- `site/_maps/` — auto-generated Jekyll collection; see scoped instructions before editing
- `cicd/update-maps/` — Python script that syncs map data from the TripleA server
- `site/user-guide/` — Markdown content pages

## Dev Workflow
- `just serve` — local server at http://localhost:4000
- `just check` — run all pre-commit hooks + jekyll build
- `just build` — build only
