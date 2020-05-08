"""
https://edabit.com/challenge/SBrK5GrreE43HgLD4
"""


def split(txt: str) -> list:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    ans, temp = [], ''
    for i, v in enumerate(txt):
        if v in vowels:
            temp += v
        elif len(temp) != 0:
            ans.append(temp)
            temp = ''
            ans.append(v)
        else:
            ans.append(v)
    if len(temp) != 0:
        ans.append(temp)
    return ans


""" Alternative solution """

import re

def split(word):
	return re.findall(r'[aeiou]+|[^aeiou]', word)


assert split("beautifully") == ["b", "eau", "t", "i", "f", "u", "l", "l", "y"]
assert split("spoonful") == ["s", "p", "oo", "n", "f", "u", "l"]
assert split("swimming") == ["s", "w", "i", "m", "m", "i", "n", "g"]
assert split("courage") == ["c", "ou", "r", "a", "g", "e"]
assert split("cooing") == ["c", "ooi", "n", "g"]

print('Success')