"""
https://edabit.com/challenge/PNbsQzmDR3CJ9JHkB
"""


def fact(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        tot = 1
        while n > 1:
            tot *= n
            n -= 1
        return tot


assert fact(0) == 1
assert fact(1) == 1
assert fact(2) == 2
assert fact(3) == 6
assert fact(7) == 5040
assert fact(9) == 362880
assert fact(15) == 1307674368000

print('Success')