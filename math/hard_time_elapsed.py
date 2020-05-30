"""
https://edabit.com/challenge/x3niK6ccbeQ5cC5kC
"""


from collections import OrderedDict


def elapsed(start, end):
    counter = OrderedDict()
    remaining = end - start
    days = remaining // (24 * 60 * 60)
    if days > 1:
        counter['days'] = days
    elif days == 1:
        counter['day'] = 1
    remaining -= days * 24 * 60 * 60
    hours = remaining // (60 * 60)
    if hours > 1:
        counter['hours'] = hours
    elif hours == 1:
        counter['hour'] = 1
    remaining -= hours * 60 * 60
    minutes = remaining // 60
    if minutes > 1:
        counter['minutes'] = minutes
    elif minutes == 1:
        counter['minute'] = 1
    remaining -= minutes * 60
    seconds = remaining
    if seconds > 1:
        counter['seconds'] = seconds
    elif seconds == 1:
        counter['second'] = 1
    L = ["{0} {1}".format(v, k) for k, v in counter.items()]
    return ', '.join(L)


assert elapsed(1559813526, 1559899926) == "1 day"
assert elapsed(1559681004, 1559899926) == "2 days, 12 hours, 48 minutes, 42 seconds"
assert elapsed(1557641659, 1559899926) == "26 days, 3 hours, 17 minutes, 47 seconds"
assert elapsed(1557652446, 1559899926) == "26 days, 18 minutes"
assert elapsed(1558773066, 1559899926) == "13 days, 1 hour, 1 minute"
assert elapsed(1552513985, 1559899926) == "85 days, 11 hours, 39 minutes, 1 second"

print("Success")