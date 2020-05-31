"""
https://edabit.com/challenge/KQ5H9aFBZDKEJuP6C
"""

import re

pattern = r'(?<!good )cookie'

lst = ['bad cookie', 'good cookie', 'bad cookie', 'good cookie', 'good cookie']

assert '(?<!' in pattern
assert len(re.findall(pattern, ', '.join(lst))) == 2

print(re.findall(pattern, ', '.join(lst)))
print("Success")
