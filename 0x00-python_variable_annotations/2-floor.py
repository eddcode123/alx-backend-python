#!/usr/bin/env python3
from math import floor as flr

"""
Provides a function to calculate the floor of a given number.
"""


def floor(n: float) -> int:
    """Calculate the largest integer less than or equal to the given number."""
    return flr(n)
