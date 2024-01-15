#!/usr/bin/env python3
"""
Module with a coroutine function returning a list of asyncio.Tasks.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Coroutine function that returns an asyncio.Task.
    """
    return asyncio.create_task(wait_random(max_delay))


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Coroutine function that returns a list of asyncio.Tasks.
    """
    tasks = [await task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
