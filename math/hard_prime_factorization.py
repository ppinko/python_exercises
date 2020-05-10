"""
https://edabit.com/challenge/gXENPxHbrqLEurbWS
"""


import math
from collections import Counter


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


def next_prime(n: int) -> int:
    while True:
        if is_prime(n):
            return n
        else:
            n += 1


def factorize(n: int) -> list:
    L, k = [], 1
    while n != 1:
        k = next_prime(k)
        while n % k == 0:
            n = n // k
            L.append(k)
        k += 1
    c = Counter(L)
    return [(k, v) for k, v in sorted(c.items(), key=lambda x: x[0])]


assert factorize(2) == [(2, 1)]
assert factorize(4) == [(2, 2)]
assert factorize(10) == [(2, 1), (5, 1)]
assert factorize(11) == [(11, 1)]
assert factorize(29) == [(29, 1)]
assert factorize(60) == [(2, 2), (3, 1), (5, 1)]
assert factorize(100) == [(2, 2), (5, 2)]
assert factorize(151) == [(151, 1)]
assert factorize(323) == [(17, 1), (19, 1)]
assert factorize(997) == [(997, 1)]
assert factorize(3349) == [(17, 1), (197, 1)]
assert factorize(5040) == [(2, 4), (3, 2), (5, 1), (7, 1)]
assert factorize(6097) == [(7, 1), (13, 1), (67, 1)]
assert factorize(8192) == [(2, 13)]
assert factorize(9870) == [(2, 1), (3, 1), (5, 1), (7, 1), (47, 1)]
assert factorize(9973) == [(9973, 1)]
assert factorize(9999) == [(3, 2), (11, 1), (101, 1)]

print('Success')