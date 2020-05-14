"""
https://edabit.com/challenge/cvxXvwRnEpekYbzzP
"""


def isprime(n: int) -> bool:
    if n <= 1 or (n % 2 == 0 and n != 2):
        return False
    elif n == 2 or n == 3:
        return True
    for i in range(3, int(pow(n, 0.5)) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_brilliant(n: int) -> bool:
    if isprime(n):
        return False
    L, k = [], 2
    while k <= n:
        while n % k == 0:
            n = n // k
            if isprime(k):
                L.append(k)
            else:
                return False
        k += 1
    if len(L) != 2:
        return False
    elif len(str(L[0])) == len(str(L[1])):
        return True
    else:
        return False


assert is_brilliant(11) == False
assert is_brilliant(9) == True
assert is_brilliant(21) == True
assert is_brilliant(22) == False 
assert is_brilliant(1001) == False
assert is_brilliant(77) == False
assert is_brilliant(209) == True
assert is_brilliant(211) == False
assert is_brilliant(780) == False
assert is_brilliant(703) == True
assert is_brilliant(1000) == False
assert is_brilliant(1003) == True
assert is_brilliant(1008) == False
assert is_brilliant(16459) == True
assert is_brilliant(348166) == False
assert is_brilliant(768017) == True

print('Success')