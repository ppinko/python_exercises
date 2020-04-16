"""
https://edabit.com/challenge/Xkc2iAjwCap2z9N5D
"""


def has_friday_13(month: int, year: int) -> bool:
    import datetime
    day = datetime.datetime(year, month, 13)
    return day.strftime("%A") == 'Friday'


assert has_friday_13(3, 2020) == True
assert has_friday_13(10, 2017) == True
assert has_friday_13(1, 1985) == False

print("Success")