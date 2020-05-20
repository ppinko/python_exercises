"""
https://edabit.com/challenge/ZSC4mb3kR9EHv7q7a
"""


def is_right_angle(lst: list, option: str) -> bool:
    if len(lst) == 0:
        return True
    if len(lst) > 3:
        return False
    if option == 'angle':
        if sum(lst) > 180:
            return False
        elif len(lst) == 3:
            if sum(lst) != 180 or 90 not in lst:
                return False
            else:
                return True
        elif len(lst) == 2:
            if sum(lst) >= 180:
                return False
            elif 90 not in lst and sum(lst) > 90:
                return False
            else:
                return True
        else:
            if sum(lst) > 90:
                return False
            else:
                return True
    if option == 'side':
        if len(lst) < 3:
            return True
        else:
            lst.sort()
            x = lst.pop()
            if x^2 == lst[0]^2 + lst[1]^2:
                return True
    return False


assert is_right_angle([30, 60], "angle") == True 
assert is_right_angle([30, 60, 90], "angle") == True
assert is_right_angle([90], "angle") == True 
assert is_right_angle([90, 90, 90], "angle") == False
assert is_right_angle([20, 20, 20, 20], "angle") == False 
assert is_right_angle([], "angle") == True 
assert is_right_angle([90, 90], "angle") == False 
assert is_right_angle([45, 46], "angle") == False
assert is_right_angle([45, 46], "side") == True
assert is_right_angle([4, 5, 6], "side") == False
assert is_right_angle([], "side") == True
assert is_right_angle([3, 4, 5], "side") == True
assert is_right_angle([60, 60, 60], "angle") == False
assert is_right_angle([177, 2, 1], "angle") == False
assert is_right_angle([20, 20, 20, 20], "side") == False
assert is_right_angle([43], "angle") == True

print('Success')