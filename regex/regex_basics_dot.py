"""
https://edabit.com/challenge/uCGpBF99YYJNv6q7L
"""


import re

pattern = 'e.{2}'

txt = 'eta, edu, etc, ele, epa, eye, exe, emf, ete, eon, era'

assert '.' in pattern
assert re.findall(pattern, txt) == ['eta', 'edu', 'etc', 'ele', 'epa', 'eye', 'exe', 'emf', 'ete', 'eon', 'era']

print('Success')