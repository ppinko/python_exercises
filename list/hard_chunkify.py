"""
https://edabit.com/challenge/biJPWHr486Y4cPLnD
"""


def chunkify(ls: list, k: int) -> list:
    res = []
    n = 0
    while n < len(ls):
        res.append(ls[n:n+k])
        n += k
    return res


assert chunkify([2, 3, 4, 5], 2) == [[2, 3], [4, 5]]
assert chunkify([2, 3, 4, 5, 6], 2) == [[2, 3], [4, 5], [6]]
assert chunkify([2, 3, 4, 5, 6, 7], 3) == [[2, 3, 4], [5, 6, 7]]
print('Success')