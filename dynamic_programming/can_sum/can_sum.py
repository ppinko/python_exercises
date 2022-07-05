"""
Given a value N, if we want to make change for N cents, and we have infinite
supply of each of S = { S1, S2, .. , Sm} valued coins. Can we use those coins
to sum up to a given value?
"""


def can_sum(target: int, nums: list, checked=set()) -> bool:
    for num in nums:
        newTarget = target - num
        if newTarget == 0:
            return True
        elif newTarget < 0:
            continue
        elif newTarget not in checked:
            checked.add(newTarget)
            if can_sum(newTarget, nums, checked):
                return True
    return False


assert can_sum(4, [5, 3, 4, 7]) == True
assert can_sum(51, [2, 3, 5]) == True
assert can_sum(7, [2, 4]) == False

print('Success')
