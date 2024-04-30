from __future__ import annotations
import sys


if sys.version_info >= (3, 8):
    from importlib import metadata
else:
    import importlib.metadata as metadata


__all__ = [
    "metadata"
]
