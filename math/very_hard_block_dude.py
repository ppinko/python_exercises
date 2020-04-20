"""
https://edabit.com/challenge/cvsGAmtHJBNDJFBpB
"""


def can_traverse(lst: list) -> bool:
    arr = [i.count(1) for i in zip(*lst)]
    return all(True if abs(arr[i] - arr[i-1]) <= 1 else False for i in range(1, len(arr)))


assert can_traverse([
	[0, 0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 1, 0, 0, 0, 0, 0], 
	[0, 0, 1, 1, 0, 0, 1, 0, 0], 
	[0, 1, 1, 1, 1, 1, 1, 1, 0]
]) == False

assert can_traverse([
	[0, 0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 1, 0, 0, 0, 0, 0], 
	[0, 0, 1, 1, 1, 0, 1, 0, 0], 
	[0, 1, 1, 1, 1, 1, 1, 1, 0]
]) == True

assert can_traverse([
	[0, 0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 1, 0, 0, 0, 0, 0], 
	[0, 0, 1, 1, 1, 1, 1, 0, 0], 
	[0, 1, 1, 1, 1, 1, 1, 1, 0]
]) == True

print('Success')