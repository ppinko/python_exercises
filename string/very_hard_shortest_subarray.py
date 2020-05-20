"""
https://edabit.com/challenge/TmasgxCm6iz3gTGHk
"""


def min_length(lst: list, n: int) -> int:
    if max(lst) > n:
        return 1
    j = 2
    while True:
        for i in range(len(lst) - j + 1):
            if sum(lst[i:i+j]) > n:
                return j
        j += 1
        if j == len(lst):
            if sum(lst) > n:
                return j
            return -1


assert min_length([1, 0, 0, 0, 1], 1) == 5
assert min_length([5, 10, 2, -1, 3, 4], 9) == 1
assert min_length([3, -1, 4, -2, -7, 2], 4) == 3
assert min_length([-5, 3, 2, 7, 8, 9, -1, 5], 16) == 2
print('Success')