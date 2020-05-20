"""
https://edabit.com/challenge/czGN5qceLFWba2j6F

Digital Egomania: the Self-Describing Numbers
"""


def is_self_describing(n: int) -> bool:
    if len(str(n)) % 2 == 1:
        return False
    return all(True if str(n).count(str(n)[i+1]) == int(str(n)[i]) else False \
            for i in range(0, len(str(n)), 2))



assert is_self_describing(10123331) == True 
assert is_self_describing(224444) == True 
assert is_self_describing(2211) == False 
assert is_self_describing(333) == False 
assert is_self_describing(1) == False
assert is_self_describing(27273332) == True
assert is_self_describing(11) == False
assert is_self_describing(22) == True
assert is_self_describing(19212332) == True
assert is_self_describing(4444332231) == False
assert is_self_describing(881722888888) == True

print('Success')