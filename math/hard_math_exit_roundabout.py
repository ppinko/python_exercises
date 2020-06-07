"""
https://edabit.com/challenge/vcxcY5cKC7Cfkt7fi
"""


def roundabout(size: int, degree: int) -> str:
    react_time, distribution = 30, 360 / size
    position = (degree + react_time) % 360
    if degree + react_time == 360:
        return "Exit 0"
    elif position % distribution == 0:
        return "Exit {0}".format(int(position // distribution))
    elif position // distribution == size - 1:
        return "Exit 0"
    else:
        return "Exit {0}".format(int(1 + position // distribution))


assert roundabout(4, 50) == "Exit 1"
assert roundabout(3, 180) == "Exit 2"
assert roundabout(6, 360) == "Exit 1"
assert roundabout(3, 100) == "Exit 2"
assert roundabout(5, 100) == "Exit 2"
assert roundabout(4, 320) == "Exit 0"
assert roundabout(2, 180) == "Exit 0"
assert roundabout(6, 250) == "Exit 5"
assert roundabout(4, 61) == "Exit 2"
assert roundabout(3, 0) == "Exit 1"
assert roundabout(4, 500) == "Exit 2"
assert roundabout(3, 68) == "Exit 1"
assert roundabout(5, 40) == "Exit 1"
assert roundabout(6, 60) == "Exit 2"

print('Success')