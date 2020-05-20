"""
https://edabit.com/challenge/SHdu4GwBQehhDm4xT
"""


def freed_prisoners(ls: list) -> int:
    free, flag = 0, True
    if ls[0] == 0:
        return free
    for i in ls:
        if flag and i == 1:
            free += 1
            flag = False
        elif not flag and i == 0:
            free += 1
            flag = True
    return free


assert freed_prisoners([1, 1, 0, 0, 0, 1, 0]) == 4
assert freed_prisoners([1, 0, 0, 0, 0, 0, 0]) == 2
assert freed_prisoners([1, 1, 1, 0, 0, 0]) == 2
assert freed_prisoners([1, 0, 1, 0, 1, 0]) == 6
print('Success')