"""
https://edabit.com/challenge/2SPQuzZTskcBpXpv4
"""

def euclidean(a, b):
    if a == b:
        return a
    if a > b:
        a = a % b
        if a == 0:
            return b
    elif a < b:
        b = b % a
        if b == 0:
            return a
    return euclidean(a, b)

#### Alternative solution

##def euclidean(a, b):
##	r = max(a, b) % min(a, b)
##	if r == 0:
##		return min(a, b)
##	else:
##		return euclidean(min(a, b), r)

print(euclidean(49, 14) == 7)
