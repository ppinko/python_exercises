"""
https://edabit.com/challenge/y5WQ54rzwEg3iga9f
"""


import math


def profit(A, B):
    remainder, middle = (A + B) % 2, (A + B) / 2
    if remainder == 0:
        return [int(middle) - 1 + 1, 100 - int(middle)]
    else:
        return [math.floor(middle) + 1, 100 - math.ceil(middle) + 1]


assert profit(32, 69) == [51, 50]
assert profit(49, 51) == [50, 50]
assert profit(25, 26) == [26, 75]
assert profit(24, 26) == [25, 75]
assert profit(0, 1) == [1, 100]
assert profit(3, 6) == [5, 96]
assert profit(55, 65) == [60, 40]
assert profit(25, 75) == [50, 50]

print('Success')