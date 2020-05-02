"""
https://edabit.com/challenge/6brSyFwWnb9Msu7kX
"""


def pos_neg_sort(lst: list) -> list:
    if len(lst) == 0:
        return []
    temp_plus = list(reversed(sorted(i for i in lst if i > 0)))
    return [i if i <= 0 else temp_plus.pop() for i in lst]


assert pos_neg_sort([6, 3, -2, 5, -8, 2, -2]) == [2, 3, -2, 5, -8, 6, -2]
assert pos_neg_sort([6, 5, 4, -1, 3, 2, -1, 1]) == [1, 2, 3, -1, 4, 5, -1, 6]
assert pos_neg_sort([-5, -5, -5, -5, 7, -5]) == [-5, -5, -5, -5, 7, -5]
assert pos_neg_sort([-5, -5, -5, -5, -4, -5]) == [-5, -5, -5, -5, -4, -5]
assert pos_neg_sort([-5, 4, -8, 3, -1, 2, 1, -7]) == [-5, 1, -8, 2, -1, 3, 4, -7]
assert pos_neg_sort([-5, 4, 3]) == [-5, 3, 4]
assert pos_neg_sort([]) == []

print('Success')