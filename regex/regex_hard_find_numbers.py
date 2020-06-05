"""
https://edabit.com/challenge/sRE3RGnWs7AHqGMkR
"""

txt = ' 123.456 2 +7 -88 -.25 9.10.11 -4. +-34 -0.6 --5 '

import re

integers = "(?<![^ ])[\+-]?\d+(?= )"
floats = "(?<![^ ])[\+-]?[\d]*\.\d+(?= )"
positive = "(?<![^ ])[\+]?[\d]*\.?\d+(?= )"
negative = "(?<![^ ])[\-][\d]*\.?\d+(?= )"
numbers = "(?<![^ ])[\-+]?[\d]*\.?\d+(?= )"


assert re.findall(integers, txt) == ['2', '+7', '-88']
assert re.findall(floats, txt) == ['123.456', '-.25', '-0.6']
assert re.findall(positive, txt) == ['123.456', '2', '+7']
assert re.findall(negative, txt) == ['-88', '-.25', '-0.6']
assert re.findall(numbers, txt) == ['123.456', '2', '+7', '-88', '-.25', '-0.6']

print('Success')
