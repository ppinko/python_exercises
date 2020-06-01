"""
https://edabit.com/challenge/deX6bsFyLWsccPakq
"""

import re

pattern = r'(?<=\s)[0-3]\d\:[0-5]\d(?![:\d])|(?<=\s)[0-2]\d\:[0-5]\d\:[0-5]\d(?!:)'

""" Alternative solution """
pattern = '(?<=[^\d:])(?:[01]\d|2[0-3])(?::[0-5]\d){1,2}(?=[,.\s])'

txt1 = 'Breakfast at 09:00 in the room 123:456.'
txt2 = 'The incident took place last Wednesday at 00:56:41.'
txt3 = 'We will have two meetings: from 10:30 to 11:00 and from 11:45 to 11:75.'
txt4 = 'Match all of these: 00:00, 04:54, 11:11:11, 23:59:59.'
txt5 = 'Do not match any of these: 00:000, 4:54, 11:11:11:11, 24:60:60.'

assert re.findall(pattern, txt1) == ['09:00']
assert re.findall(pattern, txt2) == ['00:56:41']
assert re.findall(pattern, txt3) == ['10:30', '11:00', '11:45']
assert re.findall(pattern, txt4) == ['00:00', '04:54', '11:11:11', '23:59:59']
assert re.findall(pattern, txt5) == []

print('Success')