#!/usr/bin/env python3
"""Takes a string and float or int creates a tuple."""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Create and return a tuple with the first value being the string
    followed by a float or int."""
    return k, v ** 2
