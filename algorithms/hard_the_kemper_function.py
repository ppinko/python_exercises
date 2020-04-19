"""
https://edabit.com/challenge/qQnWXBsQaH73yY8r4
"""


def kempner(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
        if total % n == 0:
            return i


assert kempner(21) == 7
assert kempner(1) == 1
assert kempner(4) == 4
print('Success')