"""
https://edabit.com/challenge/eDQDChGrv6y4fd44j
"""


def can_put(slogan, sizes):
    L = [len(i) for i in slogan.split()]
    space = [sizes[1] for i in range(sizes[0])]
    n, i = 0, 0
    while n < len(L):
        if i < len(space):
            if L[n] <= space[i]:
                space[i] -= (L[n] + 1)
                n += 1
            else:
                i += 1
        else:
            return False
    return True


assert can_put("HEY JUDE", [2, 4]) == True
assert can_put("HEY JUDE", [1, 8]) == True
assert can_put("HEY JUDE", [1, 7]) == False
assert can_put("HEY JUDE", [4, 3]) == False
assert can_put("CU L8R", [2, 2]) == False
assert can_put("CU L8R", [1, 5]) == False
assert can_put("CU L8R", [5, 5]) == True
assert can_put("BEAUTY IS WITHIN", [3, 6]) == True
assert can_put("BEAUTY IS WITHIN", [4, 5]) == False

print("Success")