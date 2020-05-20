"""
https://edabit.com/challenge/qwDPeZeufrHo2ejAY
"""


def eval_algebra(txt: str) -> int:
    L = txt.split()
    if L[4] == 'x':
        return eval(''.join(L[:3]))
    elif L[0] == 'x':
        if L[1] == '+':
            return int(L[4]) - int(L[2])
        else:
            return int(L[4]) + int(L[2])
    else:
        if L[1] == '+':
            return int(L[4]) - int(L[0])
        else:
            return -1 * (int(L[4]) - int(L[0]))


assert eval_algebra("2 + x = 19") == 17
assert eval_algebra("4 - x = 1") == 3
assert eval_algebra("23 + 1 = x") == 24
assert eval_algebra("25 - 1 = x") == 24
assert eval_algebra("x + 10 = 53") == 43
assert eval_algebra("-23 + x = -20") == 3
assert eval_algebra("10 + x = 5") == -5
assert eval_algebra("-49 - x = -180") == 131
assert eval_algebra("x + 118 = 151") == 33
assert eval_algebra("x - 46 = -2") == 44
assert eval_algebra("70 - x = -38") == 108
assert eval_algebra("-4 - 10 = x") == -14
assert eval_algebra("x - 22 = -56") == -34
assert eval_algebra("x - 57 = 62") == 119
assert eval_algebra("x + 141 = 111") == -30
assert eval_algebra("15 - 98 = x") == -83
assert eval_algebra("15 + x = 71") == 56
assert eval_algebra("-19 - 104 = x") == -123
assert eval_algebra("x + 19 = 156") == 137
assert eval_algebra("x + 65 = 155") == 90
assert eval_algebra("x + 31 = 19") == -12
assert eval_algebra("39 + 11 = x") == 50
assert eval_algebra("x - 93 = -16") == 77
assert eval_algebra("x + 95 = 216") == 121
assert eval_algebra("-21 - 108 = x") == -129
assert eval_algebra("107 - 18 = x") == 89
assert eval_algebra("x - 96 = -76") == 20
assert eval_algebra("4 + 9 = x") == 13
assert eval_algebra("52 + x = 66") == 14
assert eval_algebra("x + 45 = 64") == 19
assert eval_algebra("x - 107 = -90") == 17
assert eval_algebra("6 + x = 12") == 6
assert eval_algebra("21 + x = 58") == 37
assert eval_algebra("83 - x = -47") == 130
assert eval_algebra("x + 77 = 200") == 123
assert eval_algebra("x + 13 = 55") == 42
assert eval_algebra("-23 + x = -8") == 15
assert eval_algebra("x - 53 = 22") == 75
assert eval_algebra("x + 26 = 120") == 94
assert eval_algebra("6 + x = 60") == 54
assert eval_algebra("33 - x = 17") == 16
assert eval_algebra("105 - x = 60") == 45
assert eval_algebra("57 + x = 70") == 13
assert eval_algebra("91 + 131 = x") == 222
assert eval_algebra("-17 - 150 = x") == -167
assert eval_algebra("x - 35 = 82") == 117
assert eval_algebra("x + 56 = 21") == -35
assert eval_algebra("98 - x = -10") == 108
assert eval_algebra("x - 60 = 59") == 119
assert eval_algebra("58 + 46 = x") == 104
assert eval_algebra("-12 + 109 = x") == 97
assert eval_algebra("63 - 13 = x") == 50
assert eval_algebra("146 - x = 72") == 74
assert eval_algebra("8 - 30 = x") == -22
assert eval_algebra("28 - 78 = x") == -50
assert eval_algebra("-29 - x = -170") == 141
assert eval_algebra("69 - x = 49") == 20

print('Success')