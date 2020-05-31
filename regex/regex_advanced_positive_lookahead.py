"""
https://edabit.com/challenge/2PMS2CcnQQw487hDg
"""

import re

pattern = r'\w+(?= = yes)'
txt = 'Texas = no, California = yes, Florida = yes, Michigan = no'

assert '(?=' in pattern
assert re.findall(pattern, txt) == ['California', 'Florida']

print('Success')
