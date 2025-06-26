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
	find . -type d -name '__pycache__' -exec rm -rf {} +

real-clean: clean
	git clean -fdx
