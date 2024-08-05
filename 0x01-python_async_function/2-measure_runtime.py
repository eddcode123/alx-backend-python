#!/usr/bin/env python3
""" calculate the time it takes
to execute the wait_n function
and return the time as a flaot
"""

import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ return time in seconds it takes
    to execute a async coroutine n times
    Args:
        n: number of times to spawn wait_random
        max_delay: maximum delay between each call
    Returns:
        time in seconds
    """
    # record start time
    start_time = time.perf_counter()
    # call the coroutine
    asyncio.run(wait_n(n, max_delay))
    # record end time
    end_time = time.perf_counter()
    # calculate the time it took to run n times
    total_time = (end_time - start_time) / n

    return total_time
