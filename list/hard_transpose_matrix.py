"""
https://edabit.com/challenge/7pJZTgFstEt53f9TD
"""


def transpose_matrix(lst):
    return [list(i) for i in zip(*lst)]


assert transpose_matrix([
		[1, 1, 1],
		[2, 2, 2],
		[3, 3, 3]
	]) ==  ([
		[1, 2, 3],
		[1, 2, 3],
		[1, 2, 3]
	])

print('Success')