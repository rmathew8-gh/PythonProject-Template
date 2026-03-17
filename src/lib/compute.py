"""Core compute module with Pydantic models and business logic."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


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
    return req.a + req.b
