.DEFAULT_GOAL := help

.PHONY: help setup install-jekyll serve build clean check

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

setup: ## Install pre-commit and register it as a git push hook
	uv tool install pre-commit
	pre-commit install --hook-type pre-push

check: ## Run all validations (pre-commit hooks + jekyll build)
	pre-commit run --all-files
	bundle exec jekyll build

install-jekyll: ## Install Ruby, Jekyll, and required gems (Ubuntu/Debian)
	sudo apt install -y ruby ruby-dev make gcc
	sudo gem install bundler
	bundle install

serve: ## Start a local Jekyll server at http://localhost:4000 (auto-reloads on changes)
	bundle exec jekyll serve

build: ## Build the static site into _site/
	bundle exec jekyll build

clean: ## Remove the generated _site/ directory
	rm -rf _site/


