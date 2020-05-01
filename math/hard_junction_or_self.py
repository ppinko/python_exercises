"""
https://edabit.com/challenge/72XK73LFkd7wuakwZ
"""

from functools import reduce


def junction_or_self(n):
    ls = []
    if n < 10:
        for i in range(1, n+1):
            if 2 * i == n:
                ls.append(i)
    else:
        for i in range(1, n+1):
            if i + int(reduce(lambda x, y: int(x) + int(y), str(i))) == n:
                ls.append(i)
    if len(ls) == 0:
        return 'Self'
    ls.reverse()
    return ls


assert junction_or_self(25) == [17]
assert junction_or_self(818) == [805, 796]
assert junction_or_self(7) == "Self"
assert junction_or_self(309) == [303, 294]
assert junction_or_self(406) == [401, 392]
assert junction_or_self(188) == [175]
assert junction_or_self(20) == "Self"
assert junction_or_self(1) == "Self"
assert junction_or_self(2) == [1]
assert junction_or_self(11) == [10]
assert junction_or_self(117) == [108, 99]
assert junction_or_self(165) == "Self"

print('Success')