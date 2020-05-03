"""
https://edabit.com/challenge/6pEGXsuCAxbWTRkgc
"""


def loves_me(n: int) -> str:
    temp = ['Loves me' if i % 2 == 0 else 'Loves me not' for i in range(n)]
    temp[-1] = temp[-1].upper()
    return ', '.join(temp)


assert loves_me(1) == "LOVES ME"
assert loves_me(2) == "Loves me, LOVES ME NOT"
assert loves_me(3) == "Loves me, Loves me not, LOVES ME"

print('Success')