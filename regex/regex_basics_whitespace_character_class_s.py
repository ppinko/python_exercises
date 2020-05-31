"""
https://edabit.com/challenge/H5AQQhFhvLWMp9giA
"""

import re

pattern = r'^\s+|\s+$'

txt1 = 'Hello World'
txt3 = ' Hello World '
txt2 = '   Hello World'
txt4 = '    Hello World    '
txt5 = '    We need more space   '
txt6 = '	I    want more  room	'

assert '\s' in pattern
assert re.sub(pattern, '', txt1) == 'Hello World'
assert re.sub(pattern, '', txt2) == 'Hello World'
assert re.sub(pattern, '', txt3) == 'Hello World'
assert re.sub(pattern, '', txt4) == 'Hello World'
assert re.sub(pattern, '', txt5) == 'We need more space'
assert re.sub(pattern, '', txt6) == 'I    want more  room'

print("Success")