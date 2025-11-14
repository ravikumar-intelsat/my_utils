"""Tiny local replacement for the `my_utils` package used in examples.

This provides a single helper `format_task` so `import my_utils` works
while developing locally (avoids the broken remote editable install).
"""
from __future__ import annotations

from typing import Optional

__all__ = ["format_task", "__version__"]

__version__ = "0.0.0-dev"

def format_task(text: Optional[str]) -> str:
    """Return a small, human-friendly formatting of a task string.

    Example: "  buy milk  " -> "Buy milk"
    """
    if not text:
        return ""
    return text.strip().capitalize()
