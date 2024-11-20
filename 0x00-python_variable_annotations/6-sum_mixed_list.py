#!/usr/bin/env python3
"""Takes a mixed list of int and float and calculates their sum."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Calculates the sum of a list and returns the sum as a float """
    return sum(mxd_lst)
