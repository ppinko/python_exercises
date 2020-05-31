"""
https://edabit.com/challenge/8jwMviqNvedEmyBic
"""

import re

txt1 = 'Can read a spray chart and a balance sheet. 1 part Executive, 1 part entrepreneur, 2 parts geek and 3 parts baseball coach. Too many parts?'
txt2 = 'Can read a spray chart and a balance sheet. 1 part Executive, 1 part entrepreneur, 2 parts geek and 3 parts baseball coach. Too many parts ?'
txt3 = 'Can read a spray chart and a balance sheet. 1 part Executive, 1 part entrepreneur, 2 parts geek and 3 parts baseball coach. Too many parts  ?'

pattern = r"\S\?$"

assert '\S' in pattern
assert bool(re.search(pattern, txt1)) == True
assert bool(re.search(pattern, txt2)) == False
assert bool(re.search(pattern, txt3)) == False

print('Success')
