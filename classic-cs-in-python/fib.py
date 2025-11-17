from functools import cache
from typing import Generator
import timeit


def fib1(n: int) -> int:
    """Naive version"""
    if n < 2:
        return n

    return fib1(n - 2) + fib1(n - 1)


memo: dict[int, int] = {0: 0, 1: 1}


def fib2(n: int) -> int:
    """Manually memoized"""
    if n not in memo:
        memo[n] = fib2(n - 1) + fib2(n - 2)

    return memo[n]


@cache
def fib3(n: int) -> int:
    """Automatically memoized"""
    if n < 2:
        return n

    return fib3(n - 1) + fib3(n - 2)


def fib4(n: int) -> int:
    """Iterative version"""
    if n < 1:
        return 0

    last: int = 0  # initially set to fib(0)
    next: int = 1  # initially set to fib(1)

    for _ in range(1, n):
        last, next = next, last + next

    return next


def fib5(n: int) -> Generator[int, None, None]:
    """Generator version"""
    yield 0  # special case

    if n > 0:
        yield 1  # special case

    last: int = 0  # initially set to fib(0)
    next: int = 1  # initially set to fib(1)

    for _ in range(1, n):
        last, next = next, last + next
        yield next


if __name__ == '__main__':
    #    print(fib1(10))
    print(fib2(50))
    print(fib3(50))
    print(fib4(50))
    print(f'Time for fib2: {timeit.timeit(lambda: fib2(1000), number=10)}')
    print(f'Time for fib3: {timeit.timeit(lambda: fib3(1000), number=10)}')
    print(f'Time for fib4: {timeit.timeit(lambda: fib4(1000), number=10)}')

    for i in fib5(20):
        print(i)
