#!/usr/bin/env python3
"""Duck typing a iterable object."""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Fuction creates list of a tuple from length of elements of list """
    return [(i, len(i)) for i in lst]
