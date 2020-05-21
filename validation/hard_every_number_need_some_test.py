"""
https://edabit.com/challenge/trPQbGEb9p2yjMAWb
"""


def every_some(expr, option, *args) -> bool:
    L = [str(i) + ' ' + expr for i in args]
    if option == "everybody":
        return all(eval(i) for i in L)
    else:
        return any(eval(i) for i in L)


assert every_some(">= 1", "everybody", 1, 1, -1, 1, 1) == False
assert every_some(">= 1", "somebody", -1, -1, -1, -1, 1) == True
assert every_some("< 4 / 2", "everybody", 1, 2, 1, 2, 1, 0, -10) == False
assert every_some("!= 0", "everybody", False, False, False, False, False) == False
assert every_some("<= 10 * 2", "somebody", 21, 68, 104, 20, 3) == True
assert every_some("!= 1", "everybody", True, True, True, True, True) == False
assert every_some("== 9 % 9", "somebody", 9, 1, 81, 218, 33) == False

print('Success')