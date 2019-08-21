
import asyncio
import random

color = (
    '\033[0m',      # End of color
    '\033[36m',     # Cyan
    '\033[31m',     # Red
    '\033[35m',     # Magenta
)


async def randint(a: int, b: int) -> int:
    return random.randint(a, b)


async def make_random(idx: int, threshold: int = 6) -> int:
    print(color[idx+1] + f"Initiated make_random({idx}).")

    i = await randint(0, 10)
    while i <= threshold:
        print(color[idx+1] + f"make_random({idx}) == {i} too low; retrying.")
        await asyncio.sleep(idx + 1)
        i = await randint(0, 10)

    print(color[idx+1] + f"---> Finished: make_random({idx}) == {i}" + color[0])
    return i

async def main():
    res = await asyncio.gather(*(make_random(i, 10-i-1) for i in range(3)))
    return res

if __name__ == '__main__':
    random.seed(444)
    r1, r2, r3 = asyncio.run(main())
    print()
    print(f"r1: {r1}, r2: {r2}, r3: {r3}")

