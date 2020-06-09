"""
https://edabit.com/challenge/cwsSZhKx3QCduei7y
"""


def seq(n):
    L = [1, 2, 6]
    if n <= 2:
        return L[n]
    k = 3
    while k <= n:
        temp = 2 * L[k-1] - L[k-2] + 3
        L.append(temp)
        k += 1
    return L[n]


assert seq(1) == 2
assert seq(2) == 6
assert seq(0) == 1
assert seq(18) == 478
assert seq(27) == 1081
assert seq(6) == 52
assert seq(99) == 14653

print('Success')