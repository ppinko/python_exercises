"""
https://edabit.com/challenge/skTzXTTNQqjMnncfY
"""

import re

pattern = r"(?<=\s)(?:a|an|the) \w+"

txt1 = 'There is a pencil and a pen on the desk'
txt2 = 'They say: an apple a day keeps the doctor away'
txt3 = 'In Antarctica the temperature is quite low'
txt4 = 'Breathe the air of the mountain'
txt5 = 'He is Italian and she is French'

assert '(?:' in pattern
assert re.findall(pattern, txt1) == ['a pencil', 'a pen', 'the desk']
assert re.findall(pattern, txt2) == ['an apple', 'a day', 'the doctor']
assert re.findall(pattern, txt3) == ['the temperature']
assert re.findall(pattern, txt4) == ['the air', 'the mountain']
assert re.findall(pattern, txt5) == []

print('Success')

