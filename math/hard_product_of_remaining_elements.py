"""
https://edabit.com/challenge/JAdCy7nMK8urjv9rL
"""


def can_partition(lst: list) -> bool:
    from functools import reduce
    lst.sort()
    if reduce(lambda a, b: a * b, lst[1:]) == lst[0]:
        return True
    elif reduce(lambda a, b: a * b, lst[:-1]) == lst[-1]:
        return True
    else:
        return False


assert can_partition([-1, -10, 1, -2, 20]) == False
assert can_partition([-1, -20, 5, -1, -2, 2]) == True
assert can_partition([2, 8, 4, 1]) == True
assert can_partition([1, 1, -1, 1]) == False
assert can_partition([-1, -1, 1, 1]) == True
assert can_partition([0, 5, 1, -1]) == False
assert can_partition([0, 1, 1, -1]) == False
assert can_partition([0, 1, 1, 1]) == False
assert can_partition([0, 0, 1, 1]) == True
assert can_partition([0, 0, 1]) == True
assert can_partition([0, 0, 0]) == True
assert can_partition([5, 5, 25, 100]) == False
assert can_partition([-1, 5, 20, 100]) == False
assert can_partition([1, 1, 1, 1]) == True
assert can_partition([-1, 1, -1]) == True
assert can_partition([-1, 1, 1]) == False

print('Success')