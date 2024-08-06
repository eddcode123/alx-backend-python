#!/usr/bin/env python3
""" coroutines collects random numbers
"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ uses asyc comprehesion to
    return a list of random numbers
    between 0 and 10
    Returns:
        a list of random numbers
    """
    return [i async for i in async_generator()]
