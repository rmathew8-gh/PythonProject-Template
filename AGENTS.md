# Agent Guidelines for PythonProject-Template

When working as an AI Agent on this project, you must adhere strictly to the following guidelines and instructions, which are based on the project's configuration and `docs/cursor-guidelines-fastapi.org`.

## 1. Core Development Workflow (Makefile)
**ALWAYS use the Makefile for development tasks.** The Makefile ensures the correct environment (`uv run`) and dependencies are used.
- `make test` — Run all tests. **CRITICAL: Never run `pytest` directly; always use `make test`.**
- `make lint` — Lint and format the code using `ruff`.
- `make install` — Install dependencies using `uv`.
- `make run` — Run the application.
- `make clean` — Remove cache directories (`__pycache__`, `.pytest_cache`, `.ruff_cache`, etc.).

### Emacs compile buffers
For quick execution within Emacs, use:
```elisp
(roy/compile-and-rename "install")
(roy/compile-and-rename "lint")
(roy/compile-and-rename "test")
(roy/compile-and-rename "dev")
```

## 2. Dependency Management
- The project uses `uv` for fast dependency management. Do not use standard `pip` or `poetry` directly unless specified through `uv`.
- Dependencies are defined in the `pyproject.toml` file.

## 3. Project Organization ("src" layout)
- The project follows a strict `src/` layout. All source code must reside inside the `src/` directory, while tests reside in the `tests/` directory.
- This layout ensures packaging works correctly, imports work in "editable mode" (`uv pip install -e .` handled by `make install`), and maintains consistency between the tested code and distributed package.
- Use a **feature-based organization**: Group related module functionality together (e.g., keep business logic, models, and routes together if building an API).
- Maintain clear boundaries and a clear separation of concerns between layers.

## 4. Architecture & Design Patterns
If you are extending the application, follow these patterns from the guidelines:
- **Protocols & Dependency Injection**: Use `typing.Protocol` to define interfaces for services and data providers. Rely on dependency injection (e.g., using a DI container or FastAPI's `Depends`) rather than concrete implementations.
- **Pydantic**: Use `pydantic.BaseModel` for strictly validating data, requests, and responses.
- **Error Handling**: Use tailored exceptions and centralized exception handlers. 

## 5. Testing Best Practices
- Place shared fixtures and dependency overrides in `tests/conftest.py`.
- Prefer **Test Implementations (Fakes)** over extensive mocking. Create lightweight, stateful test implementations of your Protocols for use in tests.
- Ensure all newly added code is covered by tests. 

## 6. Code Quality
- **Linting & Formatting**: Governed by `ruff`. The maximum line length is 120. `make lint` uses formatting and unsafe fixes; ensure the code complies.
- **Type Hints**: Ensure the codebase is fully type-hinted.

## 7. Logging & Monitoring
- Prefer **structured logging** (JSON format) over generic print statements. Inject context into your logs to aid debugging.

Please review `docs/cursor-guidelines-fastapi.org` for more granular examples of these patterns when creating or refactoring code.
