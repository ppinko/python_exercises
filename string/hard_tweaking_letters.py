"""
https://edabit.com/challenge/QKyR63wENr4RMF9L7
"""


import string


def tweak_letters(word: str, lst: list) -> str:
    in_tab = string.ascii_lowercase
    out_tab_minus= 'z' + in_tab[:-1]
    out_tab_plus = in_tab[1:] + 'a'
    d_minus = dict(zip(in_tab, out_tab_minus))
    d_plus = dict(zip(in_tab, out_tab_plus))
    ans = ''
    for i, v in enumerate(lst):
        if v == 0:
            ans += word[i]
        elif v == 1:
            ans += d_plus[word[i]]
        else:
            ans += d_minus[word[i]]
    return ans


assert tweak_letters("apple", [0, 1, -1, 0, -1]) == "aqold"
assert tweak_letters("many", [0, 0, 0, -1]) == "manx"
assert tweak_letters("rhino", [1, 1, 1, 1, 1]) == "sijop"
assert tweak_letters('xyz', [1, 1, 1]) == 'yza'
assert tweak_letters('abc', [-1, -1, -1]) == 'zab'

print('Success')