"""
https://edabit.com/challenge/HXkpnCxJgxkFwaReT
"""


def count_datatypes(*args) -> list:
    res = [0] * 6
    for i in args:
        if type(i) == bool:
            res[2] += 1
        elif type(i) == int:
            res[0] += 1
        elif type(i) == str:
            res[1] += 1
        elif type(i) == list:
            res[3] += 1
        elif type(i) == tuple:
            res[4] += 1
        elif type(i) == dict:
            res[5] += 1
    return res


assert count_datatypes(1, 45, "Hi", False) == [2,1,1,0,0,0]
assert count_datatypes([10, 20], ("t", "Ok"), 2, 3, 1) == [3, 0, 0, 1, 1, 0]
assert count_datatypes("Hello", "Bye", True, True, False, {'1': 'One', '2': 'Two'}, [1, 3], {'Brayan': 18}, 25, 23) == [2, 2, 3, 1, 0, 2]
assert count_datatypes() == [0,0,0,0,0,0]
print('Success')