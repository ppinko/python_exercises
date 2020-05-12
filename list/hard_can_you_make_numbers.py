"""
https://edabit.com/challenge/LQFweeNkSNE6nwodn
"""


from collections import Counter


def can_build(nums, lst) -> bool:
    x = ''.join(str(i) for i in lst)
    c = Counter(x)
    for k, v in c.items():
        if nums[int(k)] < v:
            return False
    return True


assert can_build([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], []) == True
assert can_build([1, 1, 0, 0, 0, 0, 0, 0, 1, 0], [1, 8]) == True
assert can_build([1, 1, 0, 0, 0, 0, 0, 0, 1, 0], [1, 80]) == True
assert can_build([0, 1, 2, 2, 3, 0, 0, 0, 1, 1], [123, 444, 92]) == True
assert can_build([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [10, 23, 45, 6789]) == True
assert can_build([0, 2, 3, 0, 5, 0, 0, 0, 0, 1], [11, 2, 22, 49, 444, 4]) == True
# assert can_build([1, 1, 0, 0, 0, 0, 0, 0, 1, 0], [1, 80, 0]) == False
assert can_build([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1]) == False
# assert can_build([0, 2, 3, 0, 5, 0, 0, 0, 0, 1], [11, 7, 2, 22, 49, 444, 4]) == False
# assert can_build([0, 2, 3, 0, 5, 0, 0, 0, 0, 1], [11, 2, 22, 49, 444, 44]) == False
assert can_build([10, 2, 3, 8, 5, 8, 5, 5, 3, 1], [11, 2, 22, 49, 444, 998, 87, 44]) == False

print('Success')