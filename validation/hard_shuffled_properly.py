"""
https://edabit.com/challenge/XALogvSrMr3LRwXPH
"""


def is_shuffled_well(lst: list) -> bool:
    test_up = all(True if lst[i+1] - lst[i] != 1 or lst[i] - lst[i-1] != 1 else False
                  for i in range(1, len(lst) - 1))
    test_down = all(True if lst[i+1] - lst[i] != -1 or lst[i] - lst[i-1] != -1 else False
                    for i in range(1, len(lst) - 1))
    return test_down and test_up


assert is_shuffled_well([1, 2, 3, 5, 8, 6, 9, 10, 7, 4]) == False
assert is_shuffled_well([3, 5, 1, 9, 8, 7, 6, 4, 2, 10]) == False
assert is_shuffled_well([1, 5, 3, 8, 10, 2, 7, 6, 4, 9]) == True
assert is_shuffled_well([1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == True
assert is_shuffled_well([5, 6, 7, 9, 1, 10, 3, 8, 2, 4]) == False
assert is_shuffled_well([3, 9, 7, 5, 2, 4, 10, 1, 8, 6]) == True
assert is_shuffled_well([6, 4, 2, 1, 3, 7, 8, 10, 5, 9]) == True
assert is_shuffled_well([2, 6, 10, 9, 8, 1, 4, 7, 3, 5]) == False
assert is_shuffled_well([6, 10, 5, 8, 4, 2, 7, 9, 3, 1]) == True
assert is_shuffled_well([3, 10, 5, 2, 6, 9, 8, 4, 1, 7]) == True
assert is_shuffled_well([10, 7, 9, 5, 4, 6, 3, 8, 2, 1]) == True
assert is_shuffled_well([3, 5, 9, 6, 10, 1, 4, 8, 7, 2]) == True
assert is_shuffled_well([10, 7, 8, 4, 3, 9, 5, 1, 2, 6]) == True
assert is_shuffled_well([2, 4, 8, 7, 3, 9, 1, 10, 6, 5]) == True
assert is_shuffled_well([9, 6, 1, 3, 10, 8, 5, 4, 7, 2]) == True
assert is_shuffled_well([2, 3, 9, 7, 10, 8, 4, 6, 1, 5]) == True
assert is_shuffled_well([3, 8, 5, 6, 2, 7, 4, 1, 10, 9]) == True
assert is_shuffled_well([1, 6, 4, 10, 3, 5, 7, 2, 9, 8]) == True
assert is_shuffled_well([1, 10, 8, 9, 2, 3, 4, 7, 5, 6]) == False
assert is_shuffled_well([5, 4, 3, 10, 9, 2, 7, 6, 8, 1]) == False
assert is_shuffled_well([4, 7, 8, 3, 5, 9, 2, 6, 1, 10]) == True
assert is_shuffled_well([5, 8, 6, 7, 3, 2, 4, 9, 10, 1]) == True
assert is_shuffled_well([3, 7, 1, 4, 8, 6, 5, 9, 10, 2]) == True
assert is_shuffled_well([10, 1, 9, 4, 3, 2, 7, 8, 6, 5]) == False
assert is_shuffled_well([3, 2, 6, 4, 1, 5, 8, 10, 9, 7]) == True
assert is_shuffled_well([1, 7, 8, 5, 9, 10, 4, 6, 2, 3]) == True
assert is_shuffled_well([2, 3, 9, 7, 5, 6, 8, 1, 10, 4]) == True
assert is_shuffled_well([1, 9, 3, 4, 6, 2, 10, 8, 7, 5]) == True
assert is_shuffled_well([1, 7, 8, 5, 10, 9, 6, 4, 2, 3]) == True
assert is_shuffled_well([2, 9, 10, 3, 5, 7, 6, 4, 8, 1]) == True
assert is_shuffled_well([6, 3, 10, 8, 5, 2, 1, 9, 7, 4]) == True
assert is_shuffled_well([6, 8, 7, 3, 4, 9, 5, 10, 1, 2]) == True
assert is_shuffled_well([8, 4, 9, 5, 6, 3, 1, 10, 7, 2]) == True

print('Success')