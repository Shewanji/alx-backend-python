#!/usr/bin/env python3
"""
Measure Runtime Module
"""

import asyncio
import time
from asyncio import gather
from time import perf_counter

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime of
    executing async_comprehension four times in parallel.
    """
    start_time = perf_counter()

    await gather(*(async_comprehension() for _ in range(4)))

    end_time = perf_counter()
    total_runtime = end_time - start_time
    return total_runtime
