"""
https://edabit.com/challenge/aMTXfakahQ45oZbJP
"""


def complete_bracelet(lst: list) -> bool:
    if len(lst) < 4:
        return False
    for i in range(2, (len(lst) // 2) + 1):
        if lst[:i] == lst[-i:] and len(lst) % i == 0:
            return True
    return False


assert complete_bracelet([1, 2, 2, 1, 2, 2]) == True
assert complete_bracelet([5, 1, 2, 2]) == False
assert complete_bracelet([5, 5, 5]) == False
assert complete_bracelet([5, 5, 7, 7]) == False
assert complete_bracelet([5, 5, 7, 7, 5, 5, 7, 7]) == True
assert complete_bracelet([1, 2, 1, 2, 1, 2]) == True
assert complete_bracelet([1, 2, 2, 2, 1, 2, 2]) == False

print('Success')