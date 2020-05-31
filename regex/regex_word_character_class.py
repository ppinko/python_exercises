"""
https://edabit.com/challenge/RYykpckz6nw5zBoLG
"""

import re

txt = '**^&$Regular#$%Expressions$%$$%^**'
pattern = r'\w+'

assert '\w' in pattern
assert ' '.join(re.findall(pattern, txt)) == 'Regular Expressions'

print("Success")