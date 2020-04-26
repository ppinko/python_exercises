"""
https://edabit.com/challenge/r8jXYt5dQ3puspQfJ
"""


import re


def split(txt: str) -> str:
    vowels = re.sub(r'[^aeiou]', '', txt, flags=re.I)
    consonants = re.sub(r'[aeiou]', '', txt, flags=re.I)
    return vowels + consonants


assert split("abcde") == "aebcd"
assert split("Hello!") == "eoHll!"
assert split("What's the time?") == "aeieWht's th tm?"

print('Success')