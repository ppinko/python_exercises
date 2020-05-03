"""
https://edabit.com/challenge/536BN4JhtgLb65TXr
"""


from functools import reduce


def switch_notation(lst: list, switch: str) -> list:
    if switch == 'normal':
        temp = [reduce(lambda x, y: int(x)+int(y), str(i)) for i in lst]
        temp = [int(i) if type(i) != int else i for i in temp]
    else:
        temp = [int('5' * (i // 5)) if i % 5 == 0 else int('5' * (i // 5) + str(i % 5)) for i in lst]
    return temp


assert switch_notation([3, 55, 55551], 'normal') == [3, 10, 21]
assert switch_notation([553, 55, 51], 'normal') == [13, 10, 6]
assert switch_notation([51], 'normal') == [6]
assert switch_notation([555, 55, 5], 'normal') == [15, 10, 5]
assert switch_notation([15, 29, 5, 3], 'tally') == [555, 555554, 5, 3]
assert switch_notation([3, 8, 8, 6], 'tally') == [3, 53, 53, 51]
assert switch_notation([3, 44, 8, 21], 'tally') == [3, 555555554, 53, 55551]

print('Success')