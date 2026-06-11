"""Core compute module with Pydantic models and business logic."""

from __future__ import annotations

import os
import sys

from dotenv import load_dotenv
from pydantic import BaseModel, ConfigDict


def load_environment() -> None:
    """Load environment variables from .env file and verify DATABASE_URL is set."""
    load_dotenv()

    if not os.getenv("DATABASE_URL"):
        print("Error: DATABASE_URL is not set. Ensure a .env file is present.", file=sys.stderr)
        sys.exit(1)


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
