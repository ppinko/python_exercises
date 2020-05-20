"""
https://edabit.com/challenge/zzibM5MaxDNvQCrEk
"""


def will_fit(sizes, lst):
    for k, v in zip(sizes, lst):
        if k == 'S' and v <= 50:
            continue
        elif k == 'M' and v <= 100:
            continue
        elif k == 'L' and v <= 200:
            continue
        else:
            return False
    return True


assert will_fit(["M", "L", "L", "M"], [56, 62, 84, 90]) == True
assert will_fit(["L", "L", "M"], [56, 62, 84, 90]) == True
assert will_fit(["S", "S", "S", "S", "L"], [40, 50, 60, 70 , 80, 90, 200]) == False
assert will_fit(["S", "L"], [73 , 87, 95, 229]) == False
assert will_fit(["L", "L", "L", "L"], [54, 54, 200, 200, 200]) == True

print('Success')