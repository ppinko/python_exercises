"""
https://edabit.com/challenge/5qmRdEpAm6NQqc9JL
"""


import datetime


def hemisphere_season(hemisphere, date) -> str:
    months_conversion = {
        'Jan': 1,
        'Feb': 2,
        'Mar': 3,
        'Apr': 4,
        'May': 5,
        'Jun': 6,
        'Jul': 7,
        'Aug': 8,
        'Sep': 9,
        'Oct': 10,
        'Nov': 11,
        'Dec': 12
    }
    day_to_check = date.split()
    day_to_check[0] = str(months_conversion[day_to_check[0][:3]])
    day_to_check.append(str(2000))
    day_to_check = '-'.join(day_to_check)
    date_object = datetime.datetime.strptime(day_to_check, '%m-%d-%Y')
    if date_object <= datetime.datetime(2000, 2, 28):
        ans = ['Winter', 'Summer']
    elif date_object <= datetime.datetime(2000, 5, 31):
        ans = ['Spring', 'Autumn']
    elif date_object <= datetime.datetime(2000, 8, 31):
        ans = ['Summer', 'Winter']
    elif date_object <= datetime.datetime(2000, 11, 30):
        ans = ['Autumn', 'Spring']
    else:
        ans = ['Winter', 'Summer']

    if hemisphere == 'N':
        return ans[0]
    else:
        return ans[1]


assert hemisphere_season("N", "June, 30") == "Summer"
assert hemisphere_season("N", "March, 1") == "Spring"
assert hemisphere_season("S", "September, 22") == "Spring"
assert hemisphere_season("S", "April, 20") == "Autumn"
assert hemisphere_season("N", "November, 20") == "Autumn"
assert hemisphere_season("S", "May, 8") == "Autumn"
assert hemisphere_season("N", "February, 28") == "Winter"
assert hemisphere_season("S", "August, 6") == "Winter"
assert hemisphere_season("N", "July, 28") == "Summer"
assert hemisphere_season("S", "October, 12") == "Spring"
assert hemisphere_season("N", "December, 31") == "Winter"
assert hemisphere_season("S", "January, 2") == "Summer"

print('Success')