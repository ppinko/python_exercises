"""
https://edabit.com/challenge/fDfh3WJPPiiJwgTrW
"""

##def num_of_sublists(lst):
##	count = 0
##	for e in lst:
##		if type(e) == list:
##			count += 1
##	return count

"""
Alternative solution
"""
def num_of_sublists(lst):
    return sum(isinstance(i, list) for i in lst)

print(num_of_sublists([[1, 2, 3], [1, 2, 3], [1, 2, 3]]) == 3)

