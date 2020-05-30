"""
https://edabit.com/challenge/FSRLWWcvPRRdnuDpv
"""


def time_to_eat(time: str) -> list:
    meals = (7, 12, 19)
    temp = [int(i) for i in time.split()[0].split(':')]
    if 'p.m.' in time:
        temp[0] += 12

    if temp[0] < meals[0]:
        if temp[1] == 0:
            return [meals[0] - temp[0], temp[1]]
        else:
            return [meals[0] - temp[0] - 1, 60 - temp[1]]
    elif temp[0] < meals[1]:
        if temp[1] == 0:
            return [meals[1] - temp[0], temp[1]]
        else:
            return [meals[1] - temp[0] - 1, 60 - temp[1]]
    elif temp[0] < meals[2]:
        if temp[1] == 0:
            return [meals[2] - temp[0], temp[1]]
        else:
            return [meals[2] - temp[0] - 1, 60 - temp[1]]
    else:
        if temp[1] == 0:
            return [meals[0] + 24 - temp[0], temp[1]]
        else:
            return [meals[0] + 24 - temp[0] - 1, 60 - temp[1]]


assert time_to_eat("2:00 p.m.") == [5, 0]
assert time_to_eat("5:50 a.m.") == [1, 10]
assert time_to_eat("6:37 p.m.") == [0, 23]
assert time_to_eat("12:00 a.m.") == [7, 0]
assert time_to_eat("11:58 p.m.") == [7, 2]
assert time_to_eat("3:33 p.m.") == [3, 27]

print('Success')