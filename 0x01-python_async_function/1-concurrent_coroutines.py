#!/usr/bin/env python3
"""multiple coroutines at the same time with async"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Function runs mulitple coroutines
    Args:
        n (int): times to call max_random
        max_delay (int): seconds to delay. Default is 10
    Returns:
        list[floats]: List of delays in ascending order
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
