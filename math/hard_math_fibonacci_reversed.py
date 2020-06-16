"""
https://edabit.com/challenge/s2NZBSsYDzQKCJa3z
"""


def icc_minus_fib(n):
    if n <= 8:
        return 0
    Lf, Li = [8, 13], [8, 13]
    k = 8
    while k < n:
        k += 1
        Lf.append(Lf[-1] + Lf[-2])
        last, before_last = str(Li[-1]), str(Li[-2])
        Li.append(int(last[::-1]) + int(before_last[::-1]))
    return Li.pop() - Lf.pop()


assert icc_minus_fib(4) ==0
assert icc_minus_fib(9) ==18
assert icc_minus_fib(11) ==459
assert icc_minus_fib(20) ==9675657
assert icc_minus_fib(33) ==171358911
assert icc_minus_fib(18) ==790920
assert icc_minus_fib(49) ==996434352243
assert icc_minus_fib(31) ==93535758

print("Success")