# Makefile for Python starter template

.PHONY: install install-dev run lint test clean real-clean

UV_RUN = uv run --quiet

install-prod:
	uv venv --quiet --clear
	uv sync --quiet
	$(UV_RUN) pip install -e .

install:
	uv venv --quiet --clear
	uv sync --quiet
	$(UV_RUN) pip install -e ".[dev]"

run:
	$(UV_RUN) python src/example.py

lint:
	$(UV_RUN) ruff check --select W291,W292,W293 --fix .
	$(UV_RUN) ruff format .
	$(UV_RUN) ruff check --fix .

test:
	$(UV_RUN) pytest tests/

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
