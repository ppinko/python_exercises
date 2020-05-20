"""
https://edabit.com/challenge/b67PHXfgMwpD9rAeg
"""


def plus_sign(txt: str) -> bool:
    for i in range(len(txt)):
        if (i == 0 or i == len(txt) - 1) and txt[i].isalpha():
            return False
        elif txt[i].isalpha():
            if txt[i-1] != '+' or txt[i+1] != '+':
                return False
    return True


assert plus_sign("+f+d+c+#+f+") == True
assert plus_sign("+d+=3=+s+") == True
assert plus_sign("+d+k+##f+") == False
print('Success')