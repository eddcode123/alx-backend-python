#!/usr/bin/env python3
""" The code executes multiple coroutines
at the same time and returns a list of all the
delayed seconds
"""

import asyncio
import random

# import the function wait_random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay) -> list[float]:
    """ Call wait_delay n times with max_delay as
    its argument and return a list of
    the delayed seconds from each
    wait_delay call
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
