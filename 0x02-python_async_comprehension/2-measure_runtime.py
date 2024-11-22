#!/usr/bin/env python3
"""Measure runtime for 4 coroutines running in parallel"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime of 4 async_comprehension
    coroutines running in parallel.
    """
    # start time
    start = time.time()
    # create task
    tasks = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    # use gather to run the task concurrently
    await asyncio.gather(*tasks)
    # Stop time
    stop = time.time()
    # return time taken
    return stop - start
