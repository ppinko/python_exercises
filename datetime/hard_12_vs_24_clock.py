"""
https://edabit.com/challenge/G5FXsvc8hD6DqnCKx
"""


def convert_time(t: str) -> str:
    if 'm' in t:
        a = t.split()
        b = a[0].split(':')
        if 'am' == a[1]:
            if b != ['12', '00']:
                return ':'.join(b)
            else:
                return '0:00'
        else:
            b[0] = str(int(b[0]) + 12)
            return ':'.join(b)
    else:
        a = t.split(':')
        if int(a[0]) > 12:
            a[0] = str(int(a[0]) - 12)
            return ':'.join(a) + " pm"
        else:
            return ':'.join(a) + " am"


assert convert_time("12:00 am") == "0:00"
assert convert_time("6:20 pm") == "18:20"
assert convert_time("21:00") == "9:00 pm"
assert convert_time("5:05") == "5:05 am"

print('Success')