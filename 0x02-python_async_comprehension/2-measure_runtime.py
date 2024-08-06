#!/usr/bin/env python3
""" measure time it takes to
run a coroutine 4 times
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ execute a coroutine 4times in parallel
    using asyncio.gather method and measuring the
    time it takes to run the coroutine
    Returns:
        time in seconds
    """
    start_time = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    return time.perf_counter() - start_time
