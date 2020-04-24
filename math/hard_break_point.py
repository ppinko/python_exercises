"""
https://edabit.com/challenge/oCe79PHB7yoqkbNYb
"""


def break_point(num):
    n = str(num)
    for i in range(1, len(n)):
        a = sum(int(j) for j in n[:i])
        b = sum(int(k) for k in n[i:])
        if a == b:
            return True
    return False
    

assert break_point(159780) == True
assert break_point(112) == True
assert break_point(10) == False
assert break_point(1034) == True
assert break_point(343) == False
assert break_point(1119444) == True
assert break_point(6666) == True
assert break_point(9777771) == False
print('Success')