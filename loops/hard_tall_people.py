"""
https://edabit.com/challenge/E9FwvGyad5CDbiH4C
"""


def block(audience: list) -> int:
    return sum(len(audience) - i - 1 for i, row in enumerate(audience)
               for j in row if j == 2)


assert block([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 2], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == 2

print('Success')

