"""
https://edabit.com/challenge/fRZMqCpyxpSgmriQ6
"""


def sorting(txt: str) -> str:
    from operator import itemgetter
    digits = ''.join(sorted(i for i in txt if i.isdigit()))
    L = []
    for i in txt:
        if i.isalpha() and i.islower():
            L.append((i, i))
        elif i.isalpha() and i.isupper():
            L.append((i, i.lower()))
    L_sorted = [i[0] for i in sorted(L, key=itemgetter(1,0))]
    letters = []
    for i in L_sorted:
        if len(letters) == 0:
            letters.append(i)
        elif i == letters[-1].lower():
            letters.insert(-1, i)
        else:
            letters.append(i)
    return ''.join(letters) + digits


assert sorting("eA2a1E") == "aAeE12"
assert sorting("Re4r") == "erR4"
assert sorting("6jnM31Q") == "jMnQ136"
assert sorting("f5Eex") == "eEfx5"
assert sorting("846ZIbo") == "bIoZ468"
assert sorting("2lZduOg1jB8SPXf5rakC37wIE094Qvm6Tnyh") == "aBCdEfghIjklmnOPQrSTuvwXyZ0123456789"

print("Success")