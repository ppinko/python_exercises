"""
https://edabit.com/challenge/dHGpjWHJ265BCthiM
"""


def current_streak(today, lst) -> int:
    if len(lst) == 0:
        return 0
    from datetime import datetime, timedelta
    current = 0
    t0 = datetime.strptime(today, '%Y-%m-%d')
    while len(lst) >= 1:
        last = lst.pop()
        if last['date'] == today:
            current += 1
            continue
        t1 = datetime.strptime(last['date'], '%Y-%m-%d')
        if t0 - t1 == timedelta(current):
            current += 1
        else:
            break
    return current


print(current_streak("2019-09-23", [{"date": "2019-09-18"}, {"date": "2019-09-19"}, {"date": "2019-09-21"},
                                     {"date": "2019-09-22"}, {"date": "2019-09-23"}]))
assert current_streak("2019-09-23", [{"date": "2019-09-18"}, {"date": "2019-09-19"}, {"date": "2019-09-21"},
                                     {"date": "2019-09-22"}, {"date": "2019-09-23"}]) == 3
print('Success')