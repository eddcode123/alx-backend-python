#!/usr/bin/env python3
"""Takes a sting and float or int creates a tuple."""
from typing import Tuple, Union


def to_kv(k: str, v: Union[float, int]) -> Tuple[str, float]:
    """Create and return a tuple with the first value being the string
    followed by a float or int."""
    return (k, v)
