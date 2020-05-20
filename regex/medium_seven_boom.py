"""
https://edabit.com/challenge/BokhFunYBvsvHEjfx
"""


import re


def seven_boom(ls: list) -> str:
    if any(True if re.search(r'7', str(i)) is not None else False for i in ls):
        return "Boom!"
    else:
        return "there is no 7 in the list"


assert seven_boom([2, 6, 7, 9, 3]) == "Boom!"
assert seven_boom([33, 68, 400, 5]) == "there is no 7 in the list"
assert seven_boom([86, 48, 100, 66]) == "there is no 7 in the list"
assert seven_boom([76, 55, 44, 32]) == "Boom!"
assert seven_boom([35, 4, 9, 37]) == "Boom!"

print('Success')