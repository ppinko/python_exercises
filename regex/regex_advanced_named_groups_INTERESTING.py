"""
https://edabit.com/challenge/LMJ6HEjMuLpTd6Zzs
"""

import re

pattern = '(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})'

date1 = '2020-04-18'
date2 = '2019-10-30'
date3 = '2020-01-01'
date4 = '2020-11-14'
date5 = '1947-01-30' 
date6 = '1955-04-12'

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
m = re.search(pattern, date1)
txt = 'This challenge was posted on {} {}, {}'.format(months[int(m.group('month')) - 1], m.group('day'), m.group('year'))
print(txt)

assert txt == 'This challenge was posted on Apr 18, 2020'
for i in [date2, date3, date4, date5, date6]:
	m = re.search(pattern, i)
	assert m.group('year'), i.split('-')[0]
	assert m.group('month'), i.split('-')[1]
	assert m.group('day'), i.split('-')[2]

print('Success')