"""
https://edabit.com/challenge/fRjfrCYXWJAaQqFXF
"""
import math


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, math.ceil(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def generator_primes(num):
    n = 2
    k = 0
    while True:
        if is_prime(n):
            yield n
            k += 1
        n += 1
        if k >= num:
            raise StopIteration


def primorial(n: int) -> int:
    tot = 1
    k = 0
    for i in generator_primes(n):
        tot *= i
        k += 1
        if k == n:
            break
    return tot


assert primorial(1) == 2
assert primorial(2) == 6
assert primorial(3) == 30
assert primorial(8) == 9699690

print("Success")