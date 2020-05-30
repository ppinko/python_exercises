"""
https://edabit.com/challenge/Nr33pizZC2XdHXAm6
"""


import datetime


def months_interval(start, end) -> list:
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
              'September', 'October', 'November', 'December']
    if start > end:
        temp = start
        start = end
        end = temp

    if start == end:
        return [months[start.month - 1]]
    elif end.year - start.year > 1 or end.month - start.month == 12 or \
            (end.year - start.year == 1 and end.month - start.month >= -1):
        return months
    elif end.year == start.year:
        return months[start.month - 1: end.month]
    else:
        return months[: end.month] + months[start.month - 1:]


assert months_interval(datetime.date(2017, 1, 1), datetime.date(2017, 1, 1)) == ['January']
assert months_interval(datetime.date(2016, 1, 1), datetime.date(2017, 1, 1)) == ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
assert months_interval(datetime.date(2017, 1, 1), datetime.date(2016, 1, 1)) == ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
assert months_interval(datetime.date(2017, 4, 1), datetime.date(2017, 8, 1)) == ['April', 'May', 'June', 'July', 'August']
assert months_interval(datetime.date(2017, 8, 1), datetime.date(2017, 4, 1)) == ['April', 'May', 'June', 'July', 'August']
assert months_interval(datetime.date(2017, 12, 1), datetime.date(2018, 1, 1)) == ['January', 'December']
assert months_interval(datetime.date(2018, 1, 1), datetime.date(2017, 12, 1)) ==['January', 'December']
assert months_interval(datetime.date(2017, 4, 1), datetime.date(2019, 4, 1)) == ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
assert months_interval(datetime.date(2019, 4, 1), datetime.date(2017, 4, 1)) == ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
assert months_interval(datetime.date(2017, 4, 1), datetime.date(2043, 10, 1)) == ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
assert months_interval(datetime.date(2043, 10, 1), datetime.date(2017, 4, 1)) == ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

print('Success')