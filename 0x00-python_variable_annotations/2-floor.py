#!/usr/bin/env python3
"""
Provides a function to calculate the floor of a given number.
"""
from math import floor as flr


def floor(n: float) -> int:
    """Calculate the largest integer less than or equal to the given number."""
    return flr(n)
