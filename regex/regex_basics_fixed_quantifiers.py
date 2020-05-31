"""
https://edabit.com/challenge/e9nBwAjkdMX9LQd4f
"""

import re

txt = 'Hello!... Wait. How goes?..... GoodBye!..'
pattern = r"\.{3,}"

assert bool(re.search('\{.*\}', pattern)) == True
assert re.findall(pattern, txt) == ['...', '.....']

print('Success')