"""
https://edabit.com/challenge/k87ztfzqrpPHvgNWR
"""


def widen_streets(lst: list, n: int) -> list:
    widened = []
    transform = list(zip(*lst))
    for i, v in enumerate(lst[-1]):
        if v == '#':
            widened.append(transform[i])
        else:
            for j in range(n):
                widened.append((transform[i]))
    pre_final = list(zip(*widened))
    return [''.join(i) for i in pre_final]


assert widen_streets([
    '###   ## #',
    '### # ## #',
    '### # ## #',
    '### # ## #',
    '### # ## #'
    ], 3) == [
        '###       ##   #',
        '###   #   ##   #',
        '###   #   ##   #',
        '###   #   ##   #',
        '###   #   ##   #'
        ]

assert widen_streets([
    '## ### ###',
    '## ### ###',
    '## ### ###',
    '## ### ###' ], 2) == [ '##  ###  ###', '##  ###  ###', '##  ###  ###', '##  ###  ###' ]


print('Success')