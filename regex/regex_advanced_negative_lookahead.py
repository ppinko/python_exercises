"""
https://edabit.com/challenge/pwAdsffHkxdhSwXKc
"""

import re

pattern = r'(\w+) (?!= yes)'

txt = 'Texas = no, California = yes, Florida = yes, Michigan = no'

assert '(?!' in pattern
assert '(?=' not in pattern
assert re.findall(pattern, txt) == ['Texas', 'Michigan']

print('Success')