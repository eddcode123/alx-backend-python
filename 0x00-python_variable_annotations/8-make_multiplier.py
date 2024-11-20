#!/usr/bin/env python3
"""Creates a function that multiplies a value by the given multiplier."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Multiplies a given value by the specified multiplier.
    Args:
        multiplier (float): The value to multiply any input by.
    Returns:
        A function that multiplies a float by multiplier.
    """

    def function_multiplier(value: float) -> float:
        """Multiplies a float by multiplier"""
        return multiplier * value

    return function_multiplier
