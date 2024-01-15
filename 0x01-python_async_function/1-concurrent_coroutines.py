#!/usr/bin/env python3
"""
Async routine wait_n
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Async routine that spawns wait_random n times with the specified max_delay.
    """
    delays = []

    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)

    delays = sorted(results)

    return delays
