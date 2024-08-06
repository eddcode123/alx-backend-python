#!/usr/bin/env python3
""" coroutine that yeilds a
random value between 0, 10
"""

import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    """ this corourine loops 10 times waiting 1 second
    after each iteration then yeilds a random number
    between 0 and 10
    Arguments:
        no arguments
    Returns:
        nothing
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
