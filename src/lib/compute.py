from pydantic import BaseModel


class AddRequest(BaseModel):
    a: int
    b: int


def add(req: AddRequest) -> int:
    """Return the sum of a and b."""
    return req.a + req.b
