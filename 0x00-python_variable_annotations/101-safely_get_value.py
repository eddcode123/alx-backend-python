#!/usr/bin/env python3
"""Adding type anotation to the function below."""
from typing import Dict, TypeVar, Any, Mapping, Union

T = TypeVar('T')


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """  Safely retrieves the value of a key from a dictionary-like mapping
    Args:
        dct (Mapping[Any, T]): dictionary of key value pairs
        key (Any): a key to access value
        default (Union[T, None): Default value to return if key is invalid
    Returns:
        union(default, value): default if key is invalid and value otherwise
    """
    if key in dct:
        return dct[key]
    return default
