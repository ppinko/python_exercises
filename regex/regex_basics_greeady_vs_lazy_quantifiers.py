"""
https://edabit.com/challenge/SgKy45GqofsiDDeNs
"""

import re

txt = '... <!-- My -- comment test --> ..  <!----> .. '
pattern = r'<.+?>'

assert any(i in pattern for i in ['+?', '*?', '}?'])
assert re.findall(pattern, txt) == ['<!-- My -- comment test -->', '<!---->']

print('Success')