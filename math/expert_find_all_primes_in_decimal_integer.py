"""
https://edabit.com/challenge/T4q8P8cxvBtaLPW4q
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


def extract_primes(n: int) -> list:
    L, k = [], str(n)
    for i in k:
        if is_prime(int(i)):
            L.append(int(i))

    for i in range(len(k)):
        for j in range(i+2, len(k)+1):
            if k[i] == '0':
                continue
            elif is_prime(int(k[i:j])):
                L.append(int(k[i:j]))
    return sorted(L)


assert extract_primes(1) == []
assert extract_primes(2) == [2]
assert extract_primes(3) == [3]
assert extract_primes(13) == [3, 13]
assert extract_primes(101) == [101]
assert extract_primes(313) == [3, 3, 13, 31, 313]
assert extract_primes(10234) == [2, 3, 23]

print('Success')