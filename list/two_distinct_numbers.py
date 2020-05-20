"""
https://edabit.com/challenge/yL5WmWTCNwwb4GnR7

returnUnique([1, 9, 8, 8, 7, 6, 1, 6]) ➞ [9, 7]
returnUnique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]) ➞ [2, 1]
returnUnique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]) ➞ [5, 6]
"""

def return_unique(lst):
	ls = list()
	for element in lst:
		if lst.count(element) == 1:
			ls.append(element)
	return ls

print(return_unique([1, 9, 8, 8, 7, 6, 1, 6])) 
