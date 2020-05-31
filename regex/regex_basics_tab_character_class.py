"""
https://edabit.com/challenge/ZhCcXKviB6FZ3zz6B
"""

import re

txt = '''What	
about	
me?	 '''

pattern = '\t '

assert '\t' in pattern
assert len(re.findall(pattern, txt)) == 1

print('Success')