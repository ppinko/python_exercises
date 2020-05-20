"""
https://edabit.com/challenge/2iibnCci6G42f8Mjr
"""


def guess_score(code, guess):
    code, guess = list(code), list(guess)
    ans = {'black': 0, 'white': 0}
    remainder, rest = code[:], guess[:]
    for i, v in enumerate(code):
        if v == guess[i]:
            remainder.remove(v)
            rest.remove(v)
            ans['black'] += 1
    for j in remainder:
        if j in rest:
            rest.remove(j)
            ans['white'] += 1
    return ans


assert guess_score("1423", "5678") == {"black": 0, "white": 0}
assert guess_score("1423", "2222") == {"black": 1, "white": 0}
assert guess_score("1423", "1234") == {"black": 1, "white": 3}
assert guess_score("1423", "2211") == {"black": 0, "white": 2}
assert guess_score("2928", "7722") == {"black": 1, "white": 1}
assert guess_score("4845", "6446") == {"black": 1, "white": 1}

print('Success')