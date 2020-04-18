"""
https://edabit.com/challenge/q5FRS7dT2mrEQGG2J
"""


def has_identical(lst: list) -> bool:
    return any(True for i in zip(*lst) for j in lst if list(i) == j)


""" Alternative solution """


def has_identical2(lst):
    return any(tuple(i) in zip(*lst) for i in lst)


assert has_identical([
	[4, 4, 4, 4], 
	[2, 4, 9, 8], 
	[5, 4, 7, 7], 
	[6, 4, 1, 0]
]) == True

assert has_identical([
	[4, 4, 9, 4], 
	[2, 1, 9, 8], 
	[5, 4, 7, 7], 
	[6, 4, 1, 0]
]) == False

print('Success')