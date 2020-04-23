"""
https://edabit.com/challenge/di7ZjxgvLgz72PvCS
"""


def validate_swaps(lst, txt):
     return [False if (sum(1 for j in zip(i, txt)
                           if j[0] == j[1]) < len(txt) - 2)
                      or set(i) != set(txt) else True for i in lst]


assert validate_swaps(['BACDE', 'EBCDA', 'BCDEA', 'ACBED'], 'ABCDE') == [True, True, False, False]
assert validate_swaps(['32145', '12354', '15342', '12543'], '12345') == [True, True, True, True]
assert validate_swaps(['9786', '9788', '97865', '7689'], '9768') == [True, False, False, False]
print('Success')