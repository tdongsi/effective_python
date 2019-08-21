"""
Corountines can be chained together.
This allows you to break a pipeline into smaller, manageable coroutines (stages).
"""

import asyncio
import random
import time


async def randint(a: int, b: int) -> int:
    return random.randint(a, b)

