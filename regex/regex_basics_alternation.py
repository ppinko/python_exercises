"""
https://edabit.com/challenge/9ZAHTYWTP5c7FW4RY
"""

import re

txt1 = 'red flag blue flag'
txt2 = 'yellow flag red flag blue flag green flag'
txt3 = 'pink flag red flag black flag blue flag green flag red flag'
txt4 = 'blue flag red flag red flag blue flag green flag red flag'

pattern = "blue flag|red flag"

assert '|' in pattern
assert re.findall(pattern, txt1) == ['red flag', 'blue flag']
assert re.findall(pattern, txt2) == ['red flag', 'blue flag']
assert re.findall(pattern, txt3) == ['red flag', 'blue flag', 'red flag']
assert re.findall(pattern, txt4) == ['blue flag', 'red flag', 'red flag', 'blue flag', 'red flag']


print("Success")