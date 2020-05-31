"""
https://edabit.com/challenge/bDn2nC9GHwZMwFxRN
"""

import re

pattern = r'\Bend\B'

restricted = ['\w', '*', '.', '+']

assert any(i in pattern for i in restricted) is False
assert '\B' in pattern

txt1 = "The end of the story."
txt2 = "ending is pointless."
txt3 = "Defending the crown will end the crown!"
txt4 = "Let's send!"
txt5 = "We viewed the rendering at the end."
txt6 = "Sometimes bending the rules is good."

assert bool(re.search(pattern, txt1)) == False
assert bool(re.search(pattern, txt2)) == False
assert bool(re.search(pattern, txt3)) == True
assert bool(re.search(pattern, txt4)) == False
assert bool(re.search(pattern, txt5)) == True
assert bool(re.search(pattern, txt6)) == True

print('Success')