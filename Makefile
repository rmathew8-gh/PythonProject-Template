# Makefile for Python starter template

UV_RUN = uv run --quiet

install:
	uv venv --quiet
	uv sync --quiet
	$(UV_RUN) pip install -e .

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
