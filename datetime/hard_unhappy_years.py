"""
https://edabit.com/challenge/MSX7AHcNiCZpCsiXY
"""


def how_unlucky(year: int) -> int:
    import datetime
    return sum(1 for i in range(1, 13)
               if datetime.datetime(year, i, 13).strftime("%A") == 'Friday')


""" Alternative solution """

from datetime import date
def how_unlucky(y):
	return sum(date(y,i,13).weekday() == 4 for i in range(1,13))


assert how_unlucky(2000) == 1
assert how_unlucky(2001) == 2
assert how_unlucky(2002) == 2
assert how_unlucky(2003) == 1
assert how_unlucky(2004) == 2
assert how_unlucky(2005) == 1
assert how_unlucky(2006) == 2
assert how_unlucky(2007) == 2
assert how_unlucky(2008) == 1
assert how_unlucky(2009) == 3
assert how_unlucky(2010) == 1

print('Success')
