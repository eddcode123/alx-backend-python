#!/usr/bin/env python3
"""Creating a task."""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio task for wait_random.

    Args:
        max_delay (int): Maximum delay time.

    Returns:
        asyncio.Task: A task object for wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
