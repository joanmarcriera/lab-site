# Local checks for lab-site. Run `make check` before pushing to main.
#
# Every step uses only the stdlib Python tools in tools/ plus, when available,
# Hugo. Nothing here deploys: publishing is still `git push origin main`.

PYTHON ?= python3
# Prefer the CI-pinned binary in .bin/hugo (see CLAUDE.md), else hugo on PATH.
HUGO   ?= $(firstword $(wildcard .bin/hugo) $(shell command -v hugo 2>/dev/null))

.PHONY: check aliases test lint build

## check: run every guard below, stopping at the first failure
check: aliases test lint build

## aliases: redirect-alias guard against tests/aliases.expected.txt
aliases:
	$(PYTHON) tools/check_aliases.py

## test: unit tests under tests/
test:
	$(PYTHON) -m unittest discover -s tests -v

## lint: content linter, only when tools/content_lint.py exists
lint:
	@if [ -f tools/content_lint.py ]; then \
		echo "$(PYTHON) tools/content_lint.py"; \
		$(PYTHON) tools/content_lint.py; \
	else \
		echo "skip: tools/content_lint.py not present"; \
	fi

## build: production build into ./public, only when a Hugo binary is found
build:
	@if [ -n "$(HUGO)" ]; then \
		echo "$(HUGO) --minify"; \
		$(HUGO) --minify; \
	else \
		echo "skip: hugo not found (.bin/hugo or PATH); not built"; \
	fi
