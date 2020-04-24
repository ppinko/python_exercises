"""
https://edabit.com/challenge/d6wR7bcs4M6QdzpFj
"""


def repeat(lst, n):
	k = lst[:]
	for _ in range(n-1):
		lst.extend(k)
	return lst


def add(lst, x):
	lst.append(x)
	return lst


def remove(lst, i, j):
	k = j - i + 1
	for _ in range(k):
		lst.pop(i)
	return lst


def concat(lst, lst2):
	lst.extend(lst2)
	return lst


lst = [1, 2, 3, 4]
lst2 = [5, 6]

assert repeat(lst, 3) == [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
assert add(lst, 1) == [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1]
assert remove(lst, 1, 12) == [1]
assert concat(lst, [3, 4]) == [1, 3, 4]

# Check to make sure its a mutation, not a copy.
assert id(lst) == id(repeat(lst, 3))
assert id(lst) == id(add(lst, 1))
assert id(lst) == id(remove(lst, 1, 6))
assert id(lst) == id(concat(lst, lst2))

print('Success')