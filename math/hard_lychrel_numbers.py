"""
https://edabit.com/challenge/vSkfpeFw54mvGJeuD
"""


def ispalindrome(txt: str):
    return txt == txt[::-1]


def lychrel(n: int):
    counter = 0
    for i in range(501):
        if ispalindrome(str(n)):
            return counter
        counter += 1
        n += int(str(n)[::-1])
    return True


assert lychrel(33) == 0
assert lychrel(65) == 1
assert lychrel(348) == 3
assert lychrel(196) == True
assert lychrel(89) == 24
assert lychrel(7582) == 4
assert lychrel(1945) == True
assert lychrel(3673) == True
print('Success')