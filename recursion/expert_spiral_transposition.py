"""
https://edabit.com/challenge/5GW5Kb2RpGwhHax2W
"""


def spiral_transposition(lst: list) -> list:
    if len(lst) == 1:
        return lst[0]
    k = lst[1:]
    cols = len(k[0])
    rows = len(k)
    L = []
    for i in range(cols-1, -1, -1):
        K = []
        for j in range(rows):
            K.append(k[j][i])
        L.append(K)
    return lst[0] + spiral_transposition(L)


print(spiral_transposition([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
assert spiral_transposition([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

print('Success')