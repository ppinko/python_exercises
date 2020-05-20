"""
https://edabit.com/challenge/5ZDz5nDDPdfg5BH8K
"""


def only_5(n: int) -> bool:
    if n < 0:
        return False
    elif n % 3 == 0:
        return True
    else:
        return only_5(n-5)


def only_3(n: int) -> bool:
    if n < 0:
        return False
    elif n % 5 == 0:
        return True
    else:
        return only_3(n-3)


def only_5_and_3(n: int) -> bool:
    if n < 0:
        return False
    elif n % 3 == 0 and n % 5 == 0:
        return True
    else:
        return only_3(n-3) or only_5(n-5)


assert only_5_and_3(14) == True
assert only_5_and_3(25) == True
assert only_5_and_3(7) == False
assert only_5_and_3(2) == False
assert only_5_and_3(51) == False

print('Success')