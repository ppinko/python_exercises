"""
https://edabit.com/challenge/5h5uAmaAWY3jSHA7k
"""


def landscape_type(lst: list) -> str:
    ls = [lst[i+1] - lst[i] for i in range(len(lst) - 1) if lst[i+1] - lst[i] != 0]
    flag_valley, flag_test = False, True
    changes = 0
    for i in range(len(ls)):
        if flag_test:
            if ls[i] != 0:
                if ls[i] > 0:
                    flag_test = False
                else:
                    flag_valley = True
                    flag_test = False
        elif flag_valley:
            if ls[i] > 0:
                changes += 1
                flag_valley = False
        else:
            if ls[i] < 0:
                changes += 1
                flag_valley = True
    if changes == 0 or changes > 1:
        return 'neither'
    elif flag_valley:
        return 'mountain'
    else:
        return 'valley'


assert landscape_type([3, 4, 5, 4, 3]) == "mountain"
assert landscape_type([9, 7, 3, 1, 2, 4]) == "valley"
assert landscape_type([9, 8, 9]) == "valley"
assert landscape_type([9, 8, 9, 8]) == "neither"
print('Success')