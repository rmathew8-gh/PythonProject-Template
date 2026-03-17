"""Example usage of the compute module."""

from lib.compute import AddRequest, add


def main() -> None:
    """Run example addition."""
    req = AddRequest(a=2, b=3)
    print(f"2 + 3 = {add(req)}")


if __name__ == "__main__":
    main()
