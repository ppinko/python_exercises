"""
https://edabit.com/challenge/Egh2HES8eqPTTX9Q2
"""


def rolling_cipher(txt, n):
    import string
    if n < 0:
        while True:
            n += 26
            if n > 0:
                break
    elif n > 26:
        while True:
            n -= 26
            if n < 26:
                break
    else:
        pass
    intab = string.ascii_lowercase
    outtab = (string.ascii_lowercase * 2)[n:n+26]
    transtab = ''.maketrans(intab, outtab)
    return ''.join(i.translate(transtab) for i in txt)


""" Alternative solution """


def rolling_cipher2(txt, n):
    from string import ascii_lowercase as al
    return ''.join([al[(al.find(c)+n)%26] for c in list(txt)])


assert rolling_cipher('abcd', 1) == 'bcde'
assert rolling_cipher('abcd', -1) == 'zabc'
assert rolling_cipher('abcd', 3) == 'defg'
assert rolling_cipher('abcd', 25) == 'zabc'
assert rolling_cipher('abcd', 26) == 'abcd'
assert rolling_cipher('abcd', 27) == 'bcde'
assert rolling_cipher('abcd', 0) == 'abcd'
print('Success')