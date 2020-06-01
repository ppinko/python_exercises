"""
https://edabit.com/challenge/r8yrCWBqQrb3wmYo5
"""

import re

pattern = r"([0-9A-F]{2}:){5}[0-9A-F]{2}"

txt1 = '01:32:54:67:89:AB'
txt2 = '0132546789AB'
txt3 = '01:32:54:67:89'
txt4 = '01:32:54:67:89:ZZ'

assert bool(re.search('\(.*\)', pattern)) == True
assert bool(re.match(pattern, txt1)) == True
assert bool(re.match(pattern, txt2)) == False
assert bool(re.match(pattern, txt3)) == False
assert bool(re.match(pattern, txt4)) == False

print('Success')
