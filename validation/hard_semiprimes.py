"""
https://edabit.com/challenge/iZgvZoGZLkDPmAtNu
"""


def isprime(n: int) -> bool:
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, n // 2, 2):
        if n % i == 0:
            return False
    return True

def semiprime(n: int) -> str:
    L = []
    for i in range(2, n):
        if n % i == 0:
            L.append(i)
            n = n // i
            while n % i == 0:
                L.append(i)
                n = n // i
    if len(L) == 2 and isprime(L[0]) and L[0] == L[1]:
        return 'Semiprime'
    elif len(L) == 2 and (isprime(L[0]) or isprime(L[1])):
        return 'Squarefree Semiprime'
    else:
        return 'Neither'


assert semiprime(49) == "Semiprime"
assert semiprime(15) == "Squarefree Semiprime"
assert semiprime(19) == "Neither"
assert semiprime(75) == "Neither"
assert semiprime(169) == "Semiprime"
assert semiprime(203) == "Squarefree Semiprime"
assert semiprime(177) == "Squarefree Semiprime"
assert semiprime(125) == "Neither"
assert semiprime(70) == "Neither"

print('Success')