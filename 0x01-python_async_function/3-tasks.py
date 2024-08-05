#!/usr/bin/env python3
""" create a async task and return it
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ the function creates a async.Task
    and returns the task object
    Args:
        max_delay: maximum delay between each call
    Returns:
        task object
    """
    # create a task object
    task = asyncio.create_task(wait_random(max_delay))

    return task
