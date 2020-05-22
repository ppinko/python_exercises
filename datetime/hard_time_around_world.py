"""
https://edabit.com/challenge/fRB5QRYn5WC8jMGTe
"""


from datetime import datetime, timedelta


def time_difference(f_city, time, s_city):
    cities = {'Los Angeles':(-8, 0), 'New York':(-5, 0), 'Caracas':(-4, -30), 'Buenos Aires':(-3, 0),
              'London':(0, 0), 'Rome':(1, 0), 'Moscow':(3, 0), 'Tehran':(3, 30), 'New Delhi':(5, 30),
              'Beijing':(8, 0), 'Canberra':(10, 0)}
    day_time = datetime.strptime(time, '%B %d, %Y %H:%M')
    time_diff = (cities[s_city][0] - cities[f_city][0], cities[s_city][1] - cities[f_city][1])
    day_s_city = day_time + timedelta(hours=time_diff[0], minutes=time_diff[1])
    temp = day_s_city.strftime('%Y-%m-%d %H:%M')
    f_split = temp.split()
    s_split = f_split[0].split('-')
    t_split = [i[1:] if i[0] == '0' else i for i in s_split]
    to_join1 = '-'.join(t_split)
    return to_join1 + ' ' + f_split[1]


print(time_difference("Los Angeles", "April 1, 2011 23:23", "Canberra"))
assert time_difference("Los Angeles", "April 1, 2011 23:23", "Canberra") == "2011-4-2 17:23"
assert time_difference("London", "July 31, 1983 23:01", "Rome") == "1983-8-1 00:01"
assert time_difference("New York", "December 31, 1970 13:40", "Beijing") == "1971-1-1 02:40"
assert time_difference("London", "August 20, 1985 12:23", "Buenos Aires") == "1985-8-20 09:23"
assert time_difference("Rome", "December 21, 1987 15:11", "New Delhi") == "1987-12-21 19:41"
print(time_difference("Canberra", "March 1, 2009 18:32", "Caracas"))
assert time_difference("Canberra", "March 1, 2009 18:32", "Caracas") == "2009-3-1 04:02"
assert time_difference("Moscow", "September 14, 1953 19:54", "New York") == "1953-9-14 11:54"
assert time_difference("Beijing", "November 18, 1999 02:03", "New Delhi") == "1999-11-17 23:33"
assert time_difference("Tehran", "June 3, 1977 11:18", "Moscow") == "1977-6-3 10:48"
assert time_difference("Caracas", "January 21, 1990 12:44", "London") == "1990-1-21 17:14"
assert time_difference("New York", "February 21, 2016 17:56", "Rome") == "2016-2-21 23:56"

print('Success')