"""
https://edabit.com/challenge/gphnuvoHDANN2Fmca
"""


def odd_sort(lst: list) -> list:
    sorted_odds = sorted([i for i in lst if i % 2 == 1], reverse=True)
    return [i if i % 2 == 0 else sorted_odds.pop() for i in lst]


assert odd_sort([1, 8, 4, 3, 2, 6, 7, 5]) == [1, 8, 4, 3, 2, 6, 5, 7]
assert odd_sort([3, 7, 0, 9, 3, 2, 4, 8]) == [3, 3, 0, 7, 9, 2, 4, 8]
assert odd_sort([7, 5, 2, 3, 1]) == [1, 3, 2, 5, 7]
assert odd_sort([2, 2, 9, 7, 4, 4, 4, 9]) == [2, 2, 7, 9, 4, 4, 4, 9]
assert odd_sort([2, 2, 4, 0, 3, 1]) == [2, 2, 4, 0, 1, 3]
assert odd_sort([2, 2, 8, 4]) == [2, 2, 8, 4]
assert odd_sort([1, 9, 1]) == [1, 1, 9]

print('Success')