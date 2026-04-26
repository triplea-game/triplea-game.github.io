# TripleA Website — Copilot Instructions

## Project
Static site for [triplea-game.github.io](https://triplea-game.github.io).
Built with **Jekyll** (kramdown, SASS), hosted on **GitHub Pages**.

## Key Directories
- `_layouts/`, `_includes/` — Jekyll templates (HTML)
- `_sass/` — stylesheets
- `_maps/` — auto-generated Jekyll collection; see scoped instructions before editing
- `.build/update-maps/` — Python script that syncs map data from GitHub
- `user-guide/` — Markdown content pages

## Dev Workflow
- `make serve` — local server at http://localhost:4000
- `make check` — run all pre-commit hooks + jekyll build
- `make build` — build only

