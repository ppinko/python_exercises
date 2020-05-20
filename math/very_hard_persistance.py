"""
https://edabit.com/challenge/5ou6SKDtFRZugbpda
"""


def additive_persistence(n):
    ans = 0
    while n > 9:
        n = sum(int(i) for i in str(n))
        ans += 1
    return ans

def multiplicative_persistence(n):
    ans = 0
    while n > 9:
        k = 1
        for i in str(n):
            k *= int(i)
        ans += 1
        n = k
    return ans


assert additive_persistence(5) == 0
assert additive_persistence(27) == 1
assert multiplicative_persistence(7) == 0
assert multiplicative_persistence(1234567890) == 1
print('Success')