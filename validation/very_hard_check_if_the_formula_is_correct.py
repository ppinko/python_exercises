"""
https://edabit.com/challenge/abEZ5AEPaDBHFjfJG
"""


def formula(txt: str) -> bool:
    if len(txt) == 0:
        return None
    txt = txt.replace('a', '4')
    values = [eval(i) for i in txt.split('=')]
    return len(set(values)) == 1


assert formula('6 * 4 = 24') == True
assert formula('120 - 7 = 100') == False
assert formula('16 - 8 = 16 / 2 = 64 / 8') == True
assert formula('a = a') == True
assert formula('a * 7 = 90') == False
assert formula('16 * 10 = 160 = 14 + 120') == False
assert formula('a=4') == True
assert formula('') == None
assert formula('1000 / 10 = 100 = 2 * 50') == True
assert formula('18 / 17 = 2') == False
assert formula('(1+2+3+4+5+6+7+8)/a=9') == True
assert formula('2 * 2 * 2 = a * 2 = 8') == True
assert formula('   8/       9 =       5') == False
assert formula('1111           /     101=     11') == True
assert formula('a / a = a - 3') == True

print('Success')