"""
https://edabit.com/challenge/Hmx32xScJEm9mMH3B
"""


def longest_streak(lst: list):
    import datetime
    if len(lst) == 0:
        return "An empty list should return 0."
    if len(lst) == 1:
        return 1
    L = [i['date'] for i in lst]
    L.sort()
    days = []
    for i in L:
        a, b, c = i.split('-')
        day = datetime.datetime(int(a), int(b), int(c))
        days.append(day)
    sublist = []
    temp = 1
    for j in range(1, len(days)):
        if (days[j] - days[j-1]).days == 1:
            temp += 1
            sublist.append(temp)
        else:
            sublist.append(1)
            temp = 1
    return max(sublist)


""" Alternative solution """

from datetime import datetime, timedelta
def longest_streak(lst):
	if len(lst) in [0, 1]:
		return len(lst)
	current = 1
	max_streak = 1
	for i, j in zip(lst, lst[1:]):
		t1 = datetime.strptime(i['date'],'%Y-%m-%d')
		t2 = datetime.strptime(j['date'],'%Y-%m-%d')
		if t2-t1 == timedelta(1):
			current += 1
			max_streak = max(current, max_streak)
		else:
			current = 1
	return max_streak


assert longest_streak([
  {
    "date": "2019-09-16"
  },
  {
    "date": "2019-09-17"
  },
  {
    "date": "2019-09-21"
  },
  {
    "date": "2019-09-22"
  },
  {
    "date": "2019-09-23"
  }
]) == 3

print('Success')