"""
https://edabit.com/challenge/QN4RMpAnktNvMCWwg
"""


def id_mtrx(n):
    if not isinstance(n, int):
        return 'Error'
    if n > 0:
        return [[1 if j == i else 0 for j in range(n)] for i in range(n)]
    else:
        return [[1 if j == abs(n) - i - 1 else 0 for j in range(abs(n))] for i in range(abs(n))]


assert id_mtrx(1) == [[1]]
assert id_mtrx(2) == [[1, 0], [0, 1]]
assert id_mtrx(3) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
print(id_mtrx(-6))