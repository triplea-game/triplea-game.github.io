# triplea-game.github.io — Jekyll site: local dev, build, and validation.

set shell := ["bash", "-euo", "pipefail", "-c"]

# Show available recipes.
default:
    @just --list

# Install pre-commit and register it as a git push hook.
setup:
    uv tool install pre-commit
    pre-commit install --hook-type pre-push

# Run all validations (pre-commit hooks + jekyll build).
check:
    pre-commit run --all-files
    bundle exec jekyll build

# Install Ruby, Jekyll, and required gems (Ubuntu/Debian). Native gems need make + gcc.
install-jekyll:
    sudo apt install -y ruby ruby-dev make gcc
    sudo gem install bundler
    bundle install

# Start a local Jekyll server at http://localhost:4000 (auto-reloads on changes).
serve:
    bundle exec jekyll serve

# Build the static site into _site/.
build:
    bundle exec jekyll build

# Remove the generated _site/ directory.
clean:
    rm -rf _site/
