"""
https://edabit.com/challenge/Lx9mL2uBWwtJFv94a
"""


def checker_board(size, first, second):
    if first == second:
        return "invalid"
    L = []
    for i in range(size):
        row = []
        for j in range(size):
            if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                row.append(first)
            else:
                row.append(second)
        L.append(row)
    return L


assert checker_board(3, 'A', 'B') == [['A', 'B', 'A'],['B', 'A', 'B'],['A', 'B', 'A']]
assert checker_board(2, 7, 6) == [[7, 6], [6, 7]]

print('Success')