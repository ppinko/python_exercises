"""
https://edabit.com/challenge/MNePwAcuoKG9Cza8G
"""


def build_staircase(n: int, step: str) -> list:
    if n == 0:
        return []
    return [[step if j <= i else '_' for j in range(n)] for i in range(n)]


assert build_staircase(0, '#') == []
assert build_staircase(1, '#') == [['#']]
assert build_staircase(2, '#') == [['#', '_'], ['#', '#']]
print('Sucess')