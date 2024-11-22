#!/usr/bin/env python3
"""Async Generator."""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields random floats.

    Loops 10 times, yielding a random floating-point number between
    0 and 10, pausing for 1 second on each iteration.

    Returns:
        Generator[float, None, None]: Yields random floats between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0 , 10)
