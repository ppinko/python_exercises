"""
https://edabit.com/challenge/pDQ8sTXDxesqiTRuY
"""

import re

pattern = '(?<=tall )height'

lst = ['tall height', 'tall height', 'short height', 'medium height', 'tall height']

assert '(?<=' in pattern
assert len(re.findall(pattern, ', '.join(lst))) == 3

print('Success')