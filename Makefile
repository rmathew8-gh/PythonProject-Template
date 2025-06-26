# Makefile for Python starter template

install:
	uv venv
	uv pip install -e .

run:
	uv run python src/math_example.py

lint:
	uv run ruff check --fix .

test:
	PYTHONPATH=src uv run pytest tests/

clean:
	rm -rf __pycache__ .ruff_cache
	uv run ruff check --fix . 
