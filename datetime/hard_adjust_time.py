"""
https://edabit.com/challenge/YsD3af7LgaH6JRSCH
"""


from datetime import datetime, timedelta


def time_adjust(time, hours, minutes, seconds):
    t0_lst = [int(i) for i in time.split(':')]
    t0 = timedelta(hours=t0_lst[0], minutes=t0_lst[1], seconds=t0_lst[2])
    t1 = timedelta(hours=hours, minutes=minutes, seconds=seconds)
    t2 = t0 + t1
    if len(str(t2).split()) > 1:
        t = str(t2).split()[-1]
    else:
        t = str(t2)
    if len(t) < 8:
        return '0' + t
    else:
        return t


"""
Alternative solution
"""


def time_adjust(now, hrs, mins, sec):
	h, m, s = map(int,now.split(':'))
	s+=sec ; m+=mins+s//60 ; h+=hrs+m//60
	return '{:02d}:{:02d}:{:02d}'.format(h%24, m%60, s%60)


assert time_adjust("01:00:00", 1, 30, 10) == "02:30:10"
assert time_adjust("18:22:30", 4, 60, 30) == "23:23:00"
assert time_adjust("00:00:00", 72, 120, 120) == "02:02:00"
assert time_adjust("23:59:59", 0, 0, 1) == "00:00:00"
assert time_adjust("12:17:43", 0, 0, 0) == "12:17:43"
assert time_adjust("14:11:29", 1000, 23466, 171626) == "12:57:55"
assert time_adjust("21:02:55", 39, 62525, 332) == "22:13:27"

print("Success")