"""
https://edabit.com/challenge/juHLpxMYzfcREeMDo
"""


def col_with_max_sum(nums, n):
    tab = [nums[n*i: n*(i+1)] for i in range(len(nums) // n)]
    res = [sum(i) for i in zip(*tab)]
    return res.index(max(res)) + 1


assert col_with_max_sum([14, 9, 19, 6, 13, 13, 3, 2, 12], 3) == 3
assert col_with_max_sum([1, 13, 15, 5, 16, 1, 4, 9, 20], 3) == 2
assert col_with_max_sum([15, 4, 6, 10, 6, 4], 2) == 1
assert col_with_max_sum([7, 9, 13, 16, 17, 1, 10, 6, 3, 19, 6, 10, 8, 18, 20, 4], 8) == 7
print('Success')