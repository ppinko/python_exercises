"""
https://edabit.com/challenge/H2EyqacEnijCozCWs
"""


import re


def first_n_vowels(txt: str, n: int) -> str:
    s = ''.join(re.findall(r'[aeiou]', txt, flags=re.I))
    if len(s) >= n:
        return s[:n]
    else:
        return 'invalid'


assert first_n_vowels("sharpening skills", 3) == "aei"
assert first_n_vowels("major league", 5) == "aoeau"
assert first_n_vowels("crabby patty", 2) == "aa"
assert first_n_vowels("shrimp", 1) == "i"
assert first_n_vowels("shrimpy", 2) == "invalid"
assert first_n_vowels("hostess", 5) == "invalid"

print('Success')