from multiprocessing import Pool
import math
import functools
from pprint import pprint
import time



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


def fibonacci_executor(arr: list):
    return [fibonacci(i) for i in arr]


def factorial(arr: list):
    return [math.factorial(i) for i in arr]


def square(arr: list):
    return [i ** 2 for i in arr]


def cubic(arr: list):
    return [i ** 3 for i in arr]

def smap(f):
    return f()


if __name__ == "__main__":
    start = time.time()
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    f_fib = functools.partial(fibonacci_executor, arr)
    f_fac = functools.partial(factorial, arr)
    f_sq = functools.partial(square, arr)
    f_q = functools.partial(cubic, arr)
    with Pool() as p:
        res = p.map(smap, [f_fib, f_fac, f_sq, f_q])
        pprint(res)

    end = time.time() - start
    print(end)













