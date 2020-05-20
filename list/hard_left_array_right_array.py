"""
https://edabit.com/challenge/zW6TypLCnKKNrAqt8
"""


def left_side(lst: list) -> list:
    return [0] + [sum(1 for j in lst[:i+1] if j < v) for i, v in enumerate(lst[1:])]


def right_side(lst: list) -> list:
    return [sum(1 for j in lst[i+1:] if v > j) for i, v in enumerate(lst[:-1])] + [0]


assert left_side([5, 2, 1, 4, 8, 7]) == [0, 0, 0, 2, 4, 4]
assert left_side([3, 8, 2, 5, 4]) == [0, 1, 0, 2, 2]
assert left_side([1, 2, 3, 4, 5]) == [0, 1, 2, 3, 4]
assert right_side([5, 2, 1, 4, 8, 7]) == [3, 1, 0, 0, 1, 0]
assert right_side([3, 8, 2, 5, 4]) == [1, 3, 0, 1, 0]
assert right_side([1, 2, 3, 4, 5]) == [0, 0, 0, 0, 0]

print('Success')