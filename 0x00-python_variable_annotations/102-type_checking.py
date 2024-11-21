#!/usr/bin/env python3
"""USing mypy to correct errors"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Create a zoomed-in version of an array by repeating its elements.

    Args:
        lst (Tuple): A tuple of elements.
        factor (int): The repetition factor for each element. Defaults to 2.
    Returns:
        List: A list with elements repeated according to the factor
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
