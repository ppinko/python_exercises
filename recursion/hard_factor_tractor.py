"""
https://edabit.com/challenge/7jcWz9Kmr4rTSwdjK
"""


def rec_prime(n: int, ls: list):
    if n < 2:
        return ls
    for i in range(2, n+1):
        if n % i == 0:
            ls.append(i)
            n = int(n/i)
            return rec_prime(n, ls)


def prime_factorize(n: int) -> list:
    ls = []
    if n < 2:
        return ls
    return rec_prime(n, ls)


assert prime_factorize(32) == [2, 2, 2, 2, 2]
assert prime_factorize(17) == [17]
assert prime_factorize(35) == [5, 7]
assert prime_factorize(2) == [2]

print('Success')