"""
https://edabit.com/challenge/xbjDMxzpFcsAWKp97
"""


def can_see_stage(ls: list) -> bool:
    for i in list(zip(*ls)):
        for j in range(len(i) - 1):
            if i[j] >= i[j+1]:
                return False
    return True


assert can_see_stage([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == True
assert can_see_stage([[1, 2, 2], [1, 2, 3], [4, 4, 4]]) == False
print('Success')