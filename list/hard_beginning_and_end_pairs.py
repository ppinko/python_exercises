"""
https://edabit.com/challenge/HrCuzAKE6skEYgDmf
"""


def pairs(nums: list) -> list:
    res = []
    while len(nums) >= 2:
        res.append([nums[0], nums[-1]])
        nums = nums[1:-1]
    if len(nums) == 1:
        res.append([nums[0], nums[0]])
    return res

""" Alternative solution """


def pairs2(lst):
    x = int(len(lst)/2+.5)
    return list(map(list, zip(lst[:x], lst[::-1][:x])))


assert pairs([1, 2, 3, 4, 5, 6, 7]) == [[1, 7], [2, 6], [3, 5], [4, 4]]
assert pairs([1, 2, 3, 4, 5, 6]) == [[1, 6], [2, 5], [3, 4]]
assert pairs([5, 9, 8, 1, 2]) == [[5, 2], [9, 1], [8, 8]]
print('Success')