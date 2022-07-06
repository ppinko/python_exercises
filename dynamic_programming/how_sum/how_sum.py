"""
Given a value N, if we want to make change for N cents, and we have infinite
supply of each of S = { S1, S2, .. , Sm} valued coins. Can we use those coins
to sum up to a given value? If yes, give any solution to this task.
"""


def how_sum(target, nums, ls=[], checked=[]):
    if (target in checked) or target < 0:
        return (False, [])
    if target == 0:
        return (True, ls)
    checked.append(target)

    for num in nums:
        newTarget = target - num
        cp_ls = ls[:]
        cp_ls.append(num)
        (found, result) = how_sum(newTarget, nums, cp_ls, checked)
        if found:
            return (found, result)

    return (False, cp_ls)


(found, ls) = how_sum(4, [5, 3, 4, 7])
assert found == True
print(ls)
(found, ls) = how_sum(51, [2, 3, 5])
assert found == True
print(ls)
(found, ls) = how_sum(7, [2, 4])
assert found == False
(found, ls) = how_sum(300, [7, 14])
assert found == False

print('Success')
