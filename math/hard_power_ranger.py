"""
https://edabit.com/challenge/abdsaD6gwjgAgevsG
"""


def power_ranger(power, minimum, maximum):
    import math
    min_lvl = math.ceil(math.pow(minimum, 1 / power))
    max_lvl = math.floor(math.pow(maximum, 1 / power))
    j = 0
    for i in range(min_lvl, max_lvl + 1):
        if minimum <= math.pow(i, power) <= maximum:
            j += 1
    return j


assert power_ranger(5, 31, 33) == 1
assert power_ranger(4, 250, 1300) == 3
assert power_ranger(2, 49, 65) == 2

print("Success")
