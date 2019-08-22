"""
Demo using asyncio.Queue()
"""

import asyncio
import itertools as it
import os
import random
import time


async def make_item(size: int = 5) -> str:
    """ Return a random hex string from a random bytes object. """
    return os.urandom(size).hex()


async def randint(a: int, b: int) -> int:
    """ Asynchronous version of random.randint. """
    return random.randint(a, b)


async def randsleep(a: int = 1, b: int = 5, caller=None) -> None:
    """ Random sleep. """
    i = await randint(a, b)
    if caller:
        print(f"{caller} sleeping for {i} seconds.")
    await asyncio.sleep(i)


async def produce(name: int, q: asyncio.Queue) -> None:
    n = await randint(1, 5)

    for _ in it.repeat(None, n):   # Synchronous loop for each producer
        await randsleep(caller=f"Producer {name}")
        item = await make_item()
        timestamp = time.perf_counter()
        await q.put((item, timestamp))
        print(f"Producer {name} added <{item}> to queue.")


async def consume(name: int, q: asyncio.Queue) -> None:
    while True:
        await randsleep(caller=f"Consumer {name}")

        item, timestamp = await q.get()
        now = time.perf_counter()
        print(f"Consumer {name} got element <{item}> in {now - timestamp} seconds.")
        q.task_done()


async def main(producer_num: int, consumer_num: int):
    q = asyncio.Queue()
    producers = [asyncio.create_task(produce(i, q)) for i in range(producer_num)]
    consumers = [asyncio.create_task(consume(i, q)) for i in range(consumer_num)]

    await asyncio.gather(*producers)
    await q.join()  # Implies that it will wait for consumers

    for c in consumers:
        c.cancel()


if __name__ == '__main__':
    random.seed(444)

    start = time.perf_counter()
    asyncio.run(main(producer_num=5, consumer_num=10))
    elapsed = time.perf_counter() - start
    print(f"Program completed in {elapsed:0.5f} seconds.")
    pass
