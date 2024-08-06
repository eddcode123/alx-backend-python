#!/usr/bin/env python3
""" coroutine that yeilds a
random value between 0, 10
"""

import asyncio
import random


async def async_generator():
    """ this corourine loops 10 times waiting 1 second
    after each iteration then yeilds a random number
    between 0 and 10
    """
    for _ in range(10):
        asyncio.sleep(1)
        yield random.uniform(0, 10)
