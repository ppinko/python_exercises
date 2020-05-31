"""
https://edabit.com/challenge/u9rnDxsJRDdvRmFai
"""

import re

txt = 'best buy best car best friend best-boy bestguest best dressed best bet best man best deal best boyfriend'
pattern = 'best\sb\w+'

assert '\s' in pattern
assert re.findall(pattern, txt) == ['best buy', 'best bet', 'best boyfriend']

print("Success")
