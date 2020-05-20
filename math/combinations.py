"""
https://edabit.com/challenge/G9QRtAGXb9Cu368Pw
"""

def combinations(*iterable):
    if isinstance(iterable, int):
        return iterable
    tot = 1
    for i in iterable:
        if i != 0:
            tot *= i
    return tot
    
assert combinations(2) == 2
assert combinations(2, 3) ==  6
assert combinations(3, 5) == 15
assert combinations(5, 6, 7) == 210
assert combinations(5, 5, 5, 5) == 625
assert combinations(3, 6, 9) == 162
assert combinations(2, 3, 4, 5, 6, 7, 8, 9, 10) == 3628800
assert combinations(4, 5, 6) == 120
assert combinations(5, 6, 7, 8) == 1680
assert combinations(6, 7, 0) == 42

print("Success")
