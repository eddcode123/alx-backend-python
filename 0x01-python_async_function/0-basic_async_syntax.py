#!/usr/bin/env python3
"""Async coroutines."""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Function that waits for a random delay between 0 and max_delay seconds
    Args:
        max_delay(int): seconds to delay. Default is 10.
    Returns:
        Flaot: time it takes to execute coroutine
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
