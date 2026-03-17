# Makefile for Python starter template

.PHONY: help install run lint test type-check clean real-clean

UV_RUN = uv run

help:
	@echo "Available commands:"
	@echo "  install     - Install dependencies"
	@echo "  run         - Run the application"
	@echo "  lint        - Run linter and formatter"
	@echo "  test        - Run all tests"
	@echo "  type-check  - Run type checker (mypy)"
	@echo "  clean       - Remove cache files"
	@echo "  real-clean  - Clean + git clean"

install:
	uv sync --quiet
	uv pip install -e ".[dev]"

run:
	$(UV_RUN) python src/example.py

lint:
	$(UV_RUN) ruff check --unsafe-fixes --fix .
	$(UV_RUN) ruff format .

test: lint
	$(UV_RUN) pytest tests/ -v

type-check:
	$(UV_RUN) mypy src/

clean:
	@find . -type d -name '__pycache__' -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name '*.egg-info' -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name '.pytest_cache' -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name '.ruff_cache' -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name '.mypy_cache' -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name '*.pyc' -delete 2>/dev/null || true
	@rm -rf build/ dist/ *.egg 2>/dev/null || true

real-clean: clean
	git clean -fdx
