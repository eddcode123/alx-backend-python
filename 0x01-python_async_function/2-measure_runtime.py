#!/usr/bin/env python3
"""Measure the average time taken to run wait_n."""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average time taken to run wait_n.

    Args:
        n (int): Number of calls to wait_n.
        max_delay (int): Maximum delay for each call.

    Returns:
        float: Average time per call in seconds.
    """
    # Start time
    start = time.time()
    # call the function
    asyncio.run(wait_n(n, max_delay))
    # Stop time
    stop = time.time()
    return (stop - start) / n
