#!/usr/bin/env python3
"""Duck typing example: safely retrieve the first element of a sequence"""
from typing import Union, Any, Sequence


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely retrieves the first element of a sequence.
    Args:
        lst (Sequence[Any]): A sequence of elements of any type.
    Returns:
        Union[Any, None]: The first element if sequence, otherwise None.
    """
    if lst:
        return lst[0]
    return None
