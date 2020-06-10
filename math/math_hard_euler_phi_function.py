"""
https://edabit.com/challenge/CZYyhsQ3ZmvN3Hq7X
"""


def is_prime(n: int) -> int:
    for i in range(2, n):
        if n % i !=0:
            return False
    return True


def prime_divisors(n: int) -> list:
    L, k = [], 2
    while n > 1:
        if n % k == 0:
            L.append(k)
            while n % k == 0:
                n = int(n // k)
        k += 1
    return L


def phi(n: int) -> int:
    tot = 1
    if n == 1:
        return tot
    elif is_prime(n):
        return n - 1

    divisors = prime_divisors(n)
    for i in range(2, n):
        flag = True
        for j in divisors:
            if i >= j and i % j == 0:
                flag = False
        if flag:
            tot += 1
    return tot


assert phi(1), 1
assert phi(3), 2
assert phi(9), 6
assert phi(19), 18
assert phi(33), 20
assert phi(51), 32
assert phi(54), 18
assert phi(86), 42
assert phi(144), 48
assert phi(209), 180
assert phi(666), 216
assert phi(1000), 400

print("Success")