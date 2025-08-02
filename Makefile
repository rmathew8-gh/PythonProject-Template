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
	$(UV_RUN) ruff format .
	$(UV_RUN) ruff check --fix .

test:
	$(UV_RUN) pytest tests/

clean:
	find . -type d -name '__pycache__' -exec rm -rf {} +

real-clean: clean
	git clean -fdx
