#!/usr/bin/env python3
"""coroutine that delays return for x seconds
the returns the seconds it delayed
"""

import asyncio
import random


async def wait_random(max_delay=10):
    """ The function uses async and random to
    delay the function return by random seconds
    then returning the seconds it delayed
    """
    delay_time = random.uniform(0, max_delay)
    await asyncio.sleep(delay_time)
    return delay_time
