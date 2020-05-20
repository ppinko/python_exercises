"""
https://edabit.com/challenge/u4rHyBDs5RM2PfNxy
"""


def count_ones(lst: list) -> int:
    total, flag = 0, True
    for i in range(1, len(lst)):
        if flag and lst[i-1] == 1 and lst[i] == 1:
            flag = False
            total += 1
        elif flag is False and lst[i] != 1:
            flag = True
    return total


assert count_ones([1, 1, 1, 1, 1]) == 1
assert count_ones([1, 1, 1, 1, 0]) == 1
assert count_ones([0, 0, 0, 0, 0]) == 0
assert count_ones([1, 0, 0, 0, 0]) == 0
assert count_ones([1, 0, 1, 0, 1]) == 0
assert count_ones([1, 0, 0, 0, 1, 0, 0, 1, 1]) == 1
assert count_ones([1, 1, 0, 1, 1, 0, 0, 1, 1]) == 3
assert count_ones([1, 0, 0, 1, 1, 0, 0, 1, 1]) == 2
assert count_ones([1, 0, 0, 1, 1, 0, 1, 1, 1]) == 2
assert count_ones([1, 0, 1, 0, 1, 0, 1, 0]) == 0
assert count_ones([1, 1, 1, 1, 0, 0, 0, 0]) == 1
assert count_ones([1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1]) == 3

print('Success')