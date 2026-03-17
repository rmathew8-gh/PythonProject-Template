"""Tests for the compute module."""

import pytest
from pydantic import ValidationError

from lib.compute import AddRequest, add


class TestAddRequest:
    """Tests for the AddRequest Pydantic model."""

    def test_valid_request(self, sample_add_request: dict) -> None:
        """Test that a valid request is accepted."""
        req = AddRequest(**sample_add_request)
        assert req.a == sample_add_request["a"]
        assert req.b == sample_add_request["b"]

    def test_valid_request_positional(self) -> None:
        """Test creating request with positional arguments."""
        req = AddRequest(a=10, b=20)
        assert req.a == 10
        assert req.b == 20

    def test_invalid_request_string_a(self, sample_add_request_invalid: dict) -> None:
        """Test that string for 'a' raises ValidationError."""
        with pytest.raises(ValidationError, match="Input should be a valid integer"):
            AddRequest(**sample_add_request_invalid)

    def test_invalid_request_string_b(self) -> None:
        """Test that string for 'b' raises ValidationError."""
        with pytest.raises(ValidationError, match="Input should be a valid integer"):
            AddRequest(a=5, b="not_a_number")

    def test_invalid_request_missing_field(self) -> None:
        """Test that missing required field raises ValidationError."""
        with pytest.raises(ValidationError):
            AddRequest(a=5)

    def test_invalid_request_extra_field(self) -> None:
        """Test that extra fields raise ValidationError with extra='forbid'."""
        with pytest.raises(ValidationError, match="Extra inputs are not permitted"):
            AddRequest(a=5, b=3, c=10)

    def test_request_with_zero(self) -> None:
        """Test that zero values are valid."""
        req = AddRequest(a=0, b=0)
        assert req.a == 0
        assert req.b == 0

    def test_request_with_negative_numbers(self) -> None:
        """Test that negative numbers are valid."""
        req = AddRequest(a=-5, b=-3)
        assert req.a == -5
        assert req.b == -3


class TestAddFunction:
    """Tests for the add function."""

    def test_add_positive_numbers(self, sample_add_request: dict) -> None:
        """Test adding two positive numbers."""
        req = AddRequest(**sample_add_request)
        result = add(req)
        assert result == sample_add_request["a"] + sample_add_request["b"]

    def test_add_with_zero(self) -> None:
        """Test adding with zero."""
        req = AddRequest(a=0, b=5)
        assert add(req) == 5

    def test_add_negative_numbers(self) -> None:
        """Test adding negative numbers."""
        req = AddRequest(a=-10, b=-5)
        assert add(req) == -15

    def test_add_mixed_sign_numbers(self) -> None:
        """Test adding numbers with mixed signs."""
        req = AddRequest(a=10, b=-3)
        assert add(req) == 7

    def test_add_large_numbers(self) -> None:
        """Test adding large numbers."""
        req = AddRequest(a=1_000_000, b=2_000_000)
        assert add(req) == 3_000_000
