"""
https://edabit.com/challenge/wwN7EwvqXKCSxzyCE
"""


def reorder_digits(lst: list, direction: str) -> list:
    return [int(''.join(sorted(str(i), reverse=(direction == 'desc')))) for i in lst ]


assert reorder_digits([515, 341, 98, 44, 211], 'asc') == [155, 134, 89, 44, 112]
assert reorder_digits([515, 341, 98, 44, 211], 'desc') == [551, 431, 98, 44, 211]
assert reorder_digits([63251, 78221], 'asc') == [12356, 12278]


print('Success')