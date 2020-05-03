"""
https://edabit.com/challenge/ZFLmA6Xjt8gNxg4KR
"""


def sum_consecutives(lst: list) -> list:
    import itertools
    return [sum(list(group)) for k, group in itertools.groupby(lst)]


assert sum_consecutives([0, 7, 7, 7, 5, 4, 9, 9, 0]) == [0, 21, 5, 4, 18, 0]
assert sum_consecutives([4, 4, 5, 6, 8, 8, 8]) == [8, 5, 6, 24]
assert sum_consecutives([-5, -5, 7, 7, 12, 0]) == [-10, 14, 12, 0]
assert sum_consecutives([2, 2, 2, 2, 2, 7]) == [10, 7]
assert sum_consecutives([2, 2, -4, 4, 5, 5, 6, 6, 6, 6, 6, 1]) == [4, -4, 4, 10, 30, 1]
assert sum_consecutives([3, 3, 3, 3, 1]) == [12, 1]
assert sum_consecutives([1, -1, -2, 2, 3, -3, 4, -4]) == [1, -1, -2, 2, 3, -3, 4, -4]

print('Success')