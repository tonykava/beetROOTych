import math
import asyncio
import time
from pprint import pprint


def fibonacci(n: int):
    a = 0
    b = 1

    if n < 0:
        print("Incorrect input")

    elif n == 0:
        return 0

    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b


async def fibonacci_executor(arr: list):
    return [fibonacci(i) for i in arr]


async def factorial(arr: list):
    return [math.factorial(i) for i in arr]


async def square(arr: list):
    return [i ** 2 for i in arr]


async def cubic(arr: list):
    return [i ** 3 for i in arr]


async def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    L = await asyncio.gather(fibonacci_executor(arr),
                             factorial(arr),
                             square(arr),
                             cubic(arr))

    pprint(L)


start = time.time()
asyncio.run(main())
end = time.time() - start
print(end)





