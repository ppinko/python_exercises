"""
https://edabit.com/challenge/ffeLkHfoGDbApgNSA
"""

import re

txt1 = 'Exception 0xAF'
txt2 = 'Exception 0x1A'
txt3 = 'Exception 0x22'
txt4 = 'Exception 0xF9'
txt5 = 'Exception 0x9H'
txt6 = 'Exception 0xf9'
txt7 = 'Exception 0xB'
txt8 = 'Exception 0xBA6C3'

pattern = r'x[A-F0-9]{2}'

assert '[' in pattern and ']' in pattern

assert re.findall(pattern, txt1) == ['xAF']
assert re.findall(pattern, txt2) == ['x1A']
assert re.findall(pattern, txt3) == ['x22']
assert re.findall(pattern, txt4) == ['xF9']
assert re.findall(pattern, txt5) == []
assert re.findall(pattern, txt6) == []
assert re.findall(pattern, txt7) == []
assert re.findall(pattern, txt8) == ['xBA']

print('Success')
