"""
https://edabit.com/challenge/6sSWKcy8ttDTvkvsL
"""


def after_n_days(days, n):
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return [week[(week.index(day) + n) % 7] for day in days]


assert after_n_days(["Monday", "Tuesday", "Friday"], 1) == ["Tuesday", "Wednesday", "Saturday"]
assert after_n_days(["Sunday", "Sunday", "Sunday"], 1) == ["Monday", "Monday", "Monday"]
assert after_n_days(["Thursday", "Monday"], 4) == ["Monday", "Friday"]
print('Success')