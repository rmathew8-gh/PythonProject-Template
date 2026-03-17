"""Shared test fixtures and configuration."""

import pytest


@pytest.fixture
def sample_add_request() -> dict:
    """Fixture providing a sample add request."""
    return {"a": 5, "b": 7}


@pytest.fixture
def sample_add_request_invalid() -> dict:
    """Fixture providing an invalid add request (string instead of int)."""
    return {"a": "not_a_number", "b": 5}
