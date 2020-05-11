"""
https://edabit.com/challenge/EWZqYT4QGMYotfQTu
"""


import string


def tap_code(txt: str) -> str:
    letters = string.ascii_lowercase.replace('k', '')
    L = [letters[5*i: 5*(i+1)] for i in range(5)]
    d_letters = {k:(i+1, j+1) for i, v in enumerate(L) for j, k in enumerate(v)}
    d_letters['k'] = (1, 3)
    if '.' not in txt:
        return ' '.join(['.' * d_letters[i][0] + ' ' + '.' * d_letters[i][1] for i in txt])
    d_letters.pop('k')
    d_rev = dict(zip(d_letters.values(), d_letters.keys()))
    L = txt.split()
    return ''.join(d_rev[(len(L[2*i]), len(L[2*i+1]))] for i in range(len(L) // 2))


assert tap_code("greeting") == ".. .. .... .. . ..... . ..... .... .... .. .... ... ... .. .."
assert tap_code("confrontation") == ". ... ... .... ... ... .. . .... .. ... .... ... ... .... .... . . .... .... .. .... ... .... ... ..."
assert tap_code("leadership") == "... . . ..... . . . .... . ..... .... .. .... ... .. ... .. .... ... ....."
assert tap_code("ankle") == ". . ... ... . ... ... . . ....."
assert tap_code("extreme") == ". ..... ..... ... .... .... .... .. . ..... ... .. . ....."
assert tap_code(".... .... ... .... ... ... .. .... .. .. .. ... .... ....") == "tonight"
assert tap_code("... . ... .... ..... .... . . ... . .... .... ..... ....") == "loyalty"
assert tap_code(".... .. . ..... .. . . ..... .... .. .... .. . . ... .") == "referral"
assert tap_code(". ..... ..... ... ... ..... .... .. . ..... .... ... .... ... .. .... ... .... ... ...") == "expression"
assert tap_code(". . .. . .. . .. .... ... ... .. .... .... .... ..... ....") == "affinity"
assert tap_code("correspondence") == ". ... ... .... .... .. .... .. . ..... .... ... ... ..... ... .... ... ... . .... . ..... ... ... . ... . ....."
assert tap_code("atmosphere") == ". . .... .... ... .. ... .... .... ... ... ..... .. ... . ..... .... .. . ....."
assert tap_code("absolute") == ". . . .. .... ... ... .... ... . .... ..... .... .... . ....."
assert tap_code("redundancy") == ".... .. . ..... . .... .... ..... ... ... . .... . . ... ... . ... ..... ...."
assert tap_code("infrastructure") == ".. .... ... ... .. . .... .. . . .... ... .... .... .... .. .... ..... . ... .... .... .... ..... .... .. . ....."
assert tap_code("... ..... ... .... .. .... ... ... .... ....") == "point"
assert tap_code("... ..... .... .. . ..... .. . . ..... .... .. . ..... ... ... . ... . .....") == "preference"
assert tap_code(".. .. .... ..... .. .... . .... . .....") == "guide"
assert tap_code(". ... .. ... . . .... .. . . . ... .... .... . ..... .... .. .. .... .... ... .... .... .. .... . ...") == "characteristic"
assert tap_code(". ... ... .... ... .. ... .. . ..... .... .. . ... . .....") == "commerce"

print('Success')