"""
https://edabit.com/challenge/p88k8yHRPTMPt4bBo
"""


import re


def count_vowels(txt: str) -> int:
    return len(re.sub('[^aAeEiIoOuU]', '', txt))


assert count_vowels("Celebration") == 5
assert count_vowels("Palm") == 1
assert count_vowels("Prediction") == 4
assert count_vowels("Suite") == 3
assert count_vowels("Quote") == 3
assert count_vowels("Portrait") == 3
assert count_vowels("Steam") == 2
assert count_vowels("Tape") == 2
assert count_vowels("Nightmare") == 3
assert count_vowels("Convention") == 4

print('Success')