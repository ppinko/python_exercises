"""
https://edabit.com/challenge/hgjdb2nm4ZwuCjtHE
"""


import re


def math_expr(txt: str) -> bool:
    return re.search(r'[a-z]', txt, flags=re.I) is None


""" My alternative solution using eval """


# def math_expr(txt: str) -> bool:
#     try:
#         eval(txt)
#     except:
#         return False
#     return True


assert math_expr("5+4") == True
assert math_expr("4 * 5") == True
assert math_expr("3*6") == True
assert math_expr("4 - 5") == True
assert math_expr("6 % 7") == True
assert math_expr("a - b") == False
assert math_expr("a - 2") == False
assert math_expr("nope") == False

print('Success')