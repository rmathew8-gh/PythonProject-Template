# Python Project Template

A starter template for modern Python projects using `uv`, `pytest`, `ruff`, and `mypy`.

## Overview

This template provides a production-ready foundation for Python projects with:

- **Dependency Management**: `uv` for fast package resolution and virtual environments
- **Testing**: `pytest` with comprehensive configuration
- **Linting & Formatting**: `ruff` for fast linting and formatting
- **Type Checking**: `mypy` for static type analysis
- **Build System**: `setuptools` for packaging

## Project Structure

```
project_root/
├── src/                      # Source code (src layout)
│   └── lib/                  # Feature-based modules
│       ├── __init__.py
│       └── compute.py        # Core business logic
├── tests/                    # Test suite
│   ├── __init__.py
│   ├── conftest.py          # Shared fixtures
│   └── test_example.py      # Module tests
├── docs/                     # Documentation
├── pyproject.toml           # Project configuration
├── Makefile                 # Development commands
├── pytest.ini               # Test configuration
├── example.env              # Environment template
├── AGENTS.md                # AI agent guidelines
└── README.md                # Project documentation
```

## Getting Started

### Prerequisites

- Python 3.12 or higher
- `uv` (install via `pip install uv` or see [https://docs.astral.sh/uv/](https://docs.astral.sh/uv/))

### Installation

```bash
make install
```

This will:
1. Create a virtual environment
2. Sync dependencies
3. Install the package in editable mode with dev dependencies

## Development

### Running the Application

```bash
make run
```

### Running Tests

```bash
make test
```

This runs linting first, then pytest with verbose output.

### Type Checking

```bash
make type-check
```

This runs mypy on the source code.

### Linting and Formatting

```bash
make lint
```

This runs ruff check with auto-fix, then ruff format.

### Cleaning

```bash
make clean      # Remove cache files
make real-clean # Clean + git clean (deletes untracked files)
```

## Configuration

### Environment Variables

Copy `example.env` to `.env` and modify values:

```bash
cp example.env .env
```

See `example.env` for available configuration options.

### pytest Options

The `pytest.ini` file configures:
- Test paths and file naming conventions
- Python path for imports
- Verbose output and short traceback format
- Strict markers and warnings disabled

## Project Configuration

See `pyproject.toml` for:
- Dependencies and optional dependency groups
- Ruff linting rules and formatting options
- MyPy type checking configuration
- Test options and markers

## Code Quality

- **Linting**: Ruff enforces PEP 8 and additional rules (E, W, F, I, B, C4, UP)
- **Formatting**: Ruff format with 120 character line length
- **Type Hints**: MyPy with strict optional checking enabled
- **Documentation**: Docstrings in Google style format

## Testing Patterns

- Shared fixtures go in `tests/conftest.py`
- Prefer test implementations (fakes) over mocks
- Use pytest markers (`@pytest.mark.unit`, `@pytest.mark.integration`, `@pytest.mark.slow`)

## License

MIT License - see LICENSE file for details.
