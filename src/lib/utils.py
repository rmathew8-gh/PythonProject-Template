import os
import sys

from dotenv import load_dotenv


def load_environment() -> None:
    """Load environment variables from .env file and verify DATABASE_URL is set."""
    load_dotenv()

    if not os.getenv("DATABASE_URL"):
        print("Error: DATABASE_URL is not set. Ensure a .env file is present.", file=sys.stderr)
        sys.exit(1)
