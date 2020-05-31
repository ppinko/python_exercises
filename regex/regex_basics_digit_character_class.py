"""
https://edabit.com/challenge/RvZfGXR3TQHjLy7mN
"""

import re

pattern = r'\d.+?\.'

txt = '123 Redding Dr. 1560 Knoxville Ave. 3030 Norwalk Dr. 5 South St.'

assert '\d' in pattern
assert re.findall(pattern, txt) == ['123 Redding Dr.', '1560 Knoxville Ave.', '3030 Norwalk Dr.', '5 South St.']

print('Success')