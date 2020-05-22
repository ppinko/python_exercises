"""
https://edabit.com/challenge/whmsRve8YQ23wZuh4
"""


dates1 = ['18-10-2016_12:09', '01-12-2017_20:32', '18-10-2016_12:04',
          '19-10-2017_16:20', '18-10-2017_16:19', '18-10-2016_16:19']


from datetime import datetime


def sort_dates(lst: list, direction: str) -> list:
    L = [datetime.strptime(i, '%d-%m-%Y_%H:%M') for i in lst]
    if direction == 'DSC':
        A = sorted(L, reverse=True)
    else:
        A = sorted(L)
    return [i.strftime('%d-%m-%Y_%H:%M') for i in A]


print(sort_dates(dates1, 'ASC'))
assert sort_dates(dates1, 'ASC') == ['18-10-2016_12:04', '18-10-2016_12:09', '18-10-2016_16:19', '18-10-2017_16:19',
                                     '19-10-2017_16:20', '01-12-2017_20:32']

assert sort_dates(dates1, 'DSC') == ['01-12-2017_20:32', '19-10-2017_16:20', '18-10-2017_16:19', '18-10-2016_16:19',
                                     '18-10-2016_12:09', '18-10-2016_12:04']

print('Success')