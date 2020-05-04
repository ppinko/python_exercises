"""
https://edabit.com/challenge/pboAYDuTv7ziJgtxC
"""


def min_turns(current: str, target: str) -> int:
    return sum(abs(int(i[0]) - int(i[1])) if abs(int(i[0]) - int(i[1])) <= 5
               else 10 - abs(int(i[0]) - int(i[1])) for i in zip(current, target))


assert min_turns("4089", "5672") == 9
assert min_turns("1732", "4444") == 9
assert min_turns("7109", "2332") == 13
assert min_turns("2391", "4984") == 10
assert min_turns("1234", "3456") == 8
assert min_turns("1111", "1100") == 2
assert min_turns("1111", "0000") == 4
assert min_turns("0000", "9999") == 4

print('Success')