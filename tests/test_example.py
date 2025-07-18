import pytest
from pydantic import ValidationError
from lib.compute import add, AddRequest


def test_add():
    req = AddRequest(a=2, b=3)
    assert add(req) == 5


def test_add_invalid():
    with pytest.raises(ValidationError):
        AddRequest(a="a", b=3)
