"""
https://edabit.com/challenge/stXWy2iufNhBo9sTW
"""


def valid_rondo(s):
    if s == 'A':
        return False
    if len(s) % 2 == 0 or len(set(s[::2])) != 1 or s[0] != 'A' or s[1] != 'B':
        return False
    letters = s[1::2]
    for i in range(1, len(letters)):
        if ord(letters[i]) - ord(letters[i-1]) != 1:
            return False
    return True


assert valid_rondo('ABACADAEAFAGAHAIAJA') == True
assert valid_rondo('ABA') == True
assert valid_rondo('ABBACCA') == False
print('Success')