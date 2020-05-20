"""
https://edabit.com/challenge/A8gEGRXqMwRWQJvBf
"""


def tic_tac_toe(ls: list) -> str:
    a = ''.join((row[0] for row in ls if len(set(row)) == 1))
    b = ''.join((row[0] for row in zip(*ls) if len(set(row)) == 1))
    c = set([ls[0][0],ls[1][1], ls[2][2]])
    d = set([ls[2][0], ls[1][1], ls[0][2]])
    if len(a) == 1:
        return a[0]
    if len(b) == 1:
        return b[0]
    if len(c) == 1:
        return c.pop()
    if len(d) == 1:
        return d.pop()
    return 'Draw'

print(tic_tac_toe([
	["O", "O", "O"],
	["O", "X", "X"],
	["E", "X", "X"]
]))
assert tic_tac_toe([
	["X", "O", "X"],
	["O", "X", "O"],
	["O", "X", "X"]
]) == "X"

assert tic_tac_toe([
	["O", "O", "O"],
	["O", "X", "X"],
	["E", "X", "X"]
]) == "O"
print("Success")