"""
https://edabit.com/challenge/5zDR5LyznNPsnEuYJ
"""

import re

txt = ' alice15@gmail.com '
pattern = r'[^\w\s]'

assert '[^' in pattern, True
print(re.findall(pattern, txt))
assert re.findall(pattern, txt) == ['@', '.']

print('Success')