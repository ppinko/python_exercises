"""
https://edabit.com/challenge/tEgFCtLjRZKaGokzJ
"""


def to_star_shorthand(txt: str) -> str:
    from itertools import groupby
    L = []
    for i, group in groupby(txt):
        k = len(list(group))
        if k > 1:
            L.append(i + '*' + str(k))
        else:
            L.append(i)
    return ''.join(L)


assert to_star_shorthand("abbccc") == "ab*2c*3"
assert to_star_shorthand("haaaappyyyyy") == "ha*4p*2y*5"
assert to_star_shorthand("77777geff") == "7*5gef*2"
assert to_star_shorthand("11223344") == "1*22*23*24*2"
assert to_star_shorthand("abc") == "abc"
assert to_star_shorthand("") == ""

print("Success")