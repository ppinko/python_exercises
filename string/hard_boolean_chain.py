"""
https://edabit.com/challenge/2t6NvMe27HtSmqC4F
"""

def boolean_and(iterable: list) -> bool:
    return all(iterable)

def boolean_or(iterable: list) -> bool:
    return any(iterable)

def boolean_xor(iterable: list) -> bool:
    flag = True
    for i in range(1, len(iterable)):
        if i == 1:
            if iterable[i-1] == True and iterable[i] == True:
                flag = False
            elif iterable[i-1] == False and iterable[i] == False:
                flag = False
            else:
                flag = True
        elif flag == True:
            if iterable[i] == True:
                flag = False                
        else:
            if iterable[i] == True:
                flag = True
    return flag

"""
Alternative solution
"""
from functools import reduce

def boolean_and(lst):
	return reduce(lambda a, b : a & b, lst)	

def boolean_or(lst):
	return reduce(lambda a, b : a | b, lst)	

def boolean_xor(lst):
	return reduce(lambda a, b : a ^ b, lst)
               
# AND tests
assert boolean_and([True, True, False, True]) == False
assert boolean_and([True, True, True, True]) == True
assert boolean_and([False, True, True, True]) == False
# OR tests
assert boolean_or([True, True, False, False]) == True
assert boolean_or([True, False, False, False]) == True
assert boolean_or([False, False, False, True, False]) == True
# XOR tests
assert boolean_xor([True, True, False, True]) == True
assert boolean_xor([True, True, False, False]) == False
assert boolean_xor([True, False, False, False]) == True
assert boolean_xor([True, False, True, False])== False

print("Success")

