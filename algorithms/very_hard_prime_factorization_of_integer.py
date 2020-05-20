"""
https://edabit.com/challenge/8vBvgJMc2uQJpD6d7
"""


def prime_factors(n: int) -> list:
    res = []
    num = n
    for i in range(2, num // 2 + 1):
        while n % i == 0:
            res.append(i)
            n = n // i
        if n == 1:
            break
    return res


assert prime_factors(20) == [2, 2, 5]
assert prime_factors(100) == [2, 2, 5, 5]
assert prime_factors(8912234) == [2, 47, 94811]
print('Success')