#!/usr/bin/env python3
""" coroutine that yeilds a random numbers between 0, 10"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ This coroutine loops 10 times, waiting 1 second
    after each iteration, then yields a random float
    between 0 and 10.
    Returns:
    An AsyncGenerator yielding random floats between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
