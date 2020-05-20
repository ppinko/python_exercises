"""
https://edabit.com/challenge/vC4P2jGR6wxED7MBL
"""


def larger_than_right(lst):
    return [v for i, v in enumerate(lst) if len(lst[i+1:]) == 0 or v > max(lst[i+1:])]


assert larger_than_right([3, 13, 11, 2, 1, 9, 5]) == [13, 11, 9, 5]
assert larger_than_right([9, 8, 7, 6]) == [9, 8, 7, 6]
assert larger_than_right([1, 2, 3, 4]) == [4]
assert larger_than_right([5, 9, 8, 7]) == [9, 8, 7]
assert larger_than_right([5, 5, 5, 5, 5]) == [5]

print('Success')