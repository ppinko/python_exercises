"""
https://edabit.com/challenge/eRY7eBD8dan54acgG
"""


def is_checkerboard(lst):
    if sum(1 if lst[i] == list(zip(*lst))[i] else 0 for i in range(len(lst))):
        return False
    for i in range(len(lst)):
        for j in range(1, len(lst)):
            if lst[i][j] == lst[i][j-1]:
                return False
    return True


assert is_checkerboard([
	[1, 0, 1, 0, 1],
	[0, 1, 0, 1, 0],
	[1, 0, 1, 0, 1],
	[0, 1, 0, 1, 0],
	[1, 0, 1, 0, 1]
]) == True

assert is_checkerboard([
	[0, 1, 0, 1, 0],
	[1, 0, 1, 0, 1],
	[0, 1, 0, 1, 0],
	[1, 0, 1, 0, 1],
	[0, 1, 0, 1, 0]
]) == True

assert is_checkerboard([
	[0, 1, 0, 1, 0],
	[1, 0, 1, 0, 1],
	[0, 1, 0, 1, 0],
	[1, 0, 1, 1, 1],
	[0, 1, 0, 1, 0]
]) == False

assert is_checkerboard([
	[0, 1, 0, 1, 0],
	[1, 0, 1, 0, 1],
	[0, 1, 0, 1, 0],
	[1, 0, 1, 0, 1],
	[1, 1, 0, 1, 0]
]) == False

assert is_checkerboard([
	[1, 0, 1, 0, 1],
	[0, 1, 0, 1, 0],
	[1, 0, 1, 0, 1],
	[0, 1, 0, 1, 0],
	[1, 0, 1, 1, 1]
]) == False

assert is_checkerboard([
	[0, 1],
	[1, 0]
]) == True

assert is_checkerboard([
	[1, 1],
	[1, 0]
]) == False

assert is_checkerboard([
	[1, 1],
	[0, 1]
]) == False

assert is_checkerboard([
	[1, 0],
	[0, 1]
]) == True

assert is_checkerboard([
	[1, 0, 1],
	[0, 1, 0],
	[1, 0, 1]
]) == True

print('Success')