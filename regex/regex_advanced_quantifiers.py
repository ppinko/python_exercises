"""
https://edabit.com/challenge/PvRttLNygmjEzeZtb
"""

import re

pattern = '(?<=, )\d[^,]+'

txt1 = 'Harry Potter, 4 Privet Drive, Little Whinging, Surrey'
txt2 = 'Sherlock Holmes, 221B Baker St, Marylebone London NW1 6XE, UK'
txt3 = 'The White House, 1600 Pennsylvania Avenue, Washington, DC'
quantifiers = ['*', '+', '?']

assert any(i in pattern for i in quantifiers) == True
assert re.findall(pattern, txt1) == ['4 Privet Drive']
assert re.findall(pattern, txt2) == ['221B Baker St']
assert re.findall(pattern, txt3) == ['1600 Pennsylvania Avenue']

print('Success')