"""Core compute module with Pydantic models and business logic."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

# use relative imports to prove they work
from .utils import load_environment


class AddRequest(BaseModel):
    """Request model for addition operation.

    Attributes:
        a: First integer operand.
        b: Second integer operand.
    """

    model_config = ConfigDict(extra="forbid")

    a: int
    b: int


def add(req: AddRequest) -> int:
    """Return the sum of a and b.

    Args:
        req: AddRequest containing the operands.

    Returns:
        The sum of the two integers.

    Example:
        >>> req = AddRequest(a=2, b=3)
        >>> add(req)
        5
    """
    load_environment()

    return req.a + req.b
