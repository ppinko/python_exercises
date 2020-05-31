"""
https://edabit.com/challenge/2TbW2br5FyNrByPHc
"""

import re

pattern = r'<\Wdiv>'

txt1 = '<div>Hello.</div><div>My name is <b>George</b>.</div>'
txt2 = '<div><h1>The Word for Today</h1><div>aardvark</div></div>'
txt3 = '<div><div><div></div></div></div>'

assert '\W' in pattern
assert len(re.findall(pattern, txt1)) == 2
assert len(re.findall(pattern, txt2)) == 2
assert len(re.findall(pattern, txt3)) == 3

print('Success')
