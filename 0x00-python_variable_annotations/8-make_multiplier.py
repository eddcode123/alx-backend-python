#!/usr/bin/env python3
"""Creates a function that multiplies a value by the given multiplier."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a given value by the specified multiplier.

    Args:
        multiplier (float): The value to multiply any input by.

    Returns:
        Callable[[float], float]: A function that takes a float and returns the product 
                                  of the input value and the multiplier.
    """
    def function_multiplier(value: float) -> float:
        return multiplier * value
    
    return function_multiplier
