#!/usr/bin/env python3
"""Defines ans asynchronous coroutine"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine tthat waits for a random delay
    between 0 and max_delay seconds"""
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
