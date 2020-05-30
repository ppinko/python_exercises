"""
https://edabit.com/challenge/Be4gGbqXMcjpkhfQg
"""


from datetime import datetime


def convert_date(date: str) -> list:
    if '/' in date:
        return [int(i) for i in date.split('/')]
    elif '-' in date:
        return [int(i) for i in date.split('-')]
    elif '.' in date:
        return [int(i) for i in date.split('.')]
    date = date.replace(',', '')
    if date[3] == ' ':
        day = datetime.strptime(date, '%b %d %Y')
    else:
        day = datetime.strptime(date, '%B %d %Y')
    return [int(i) for i in day.strftime('%m %d %Y').split()]


assert convert_date("January 9, 2019") == [1, 9, 2019]
assert convert_date("Jan 9, 2019") == [1, 9, 2019]
assert convert_date("01/09/2019") == [1, 9, 2019]
assert convert_date("01-09-2019") == [1, 9, 2019]
assert convert_date("01.09.2019") == [1, 9, 2019]
assert convert_date("March 3, 1901") == [3, 3, 1901]
assert convert_date("Mar 3, 1901") == [3, 3, 1901]
assert convert_date("03/03/1901") == [3, 3, 1901]
assert convert_date("03-03-1901") == [3, 3, 1901]
assert convert_date("03.03.1901") == [3, 3, 1901]
assert convert_date("August 8, 1666") == [8, 8, 1666]
assert convert_date("Nov 13, 1533") == [11, 13, 1533]
assert convert_date("04/15/1789") == [4, 15, 1789]
assert convert_date("12-23-1111") == [12, 23, 1111]
assert convert_date("02.28.1832") == [2, 28, 1832]

print("Success")