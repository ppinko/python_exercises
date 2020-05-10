"""
https://edabit.com/challenge/5XNKfyxBosjSXCWLn
"""


def is_modest(n: int) -> bool:
    n_str = str(n)
    return any(True if int(n_str[i:]) != 0 and n % int(n_str[i:]) == int(n_str[:i]) \
                   else False for i in range(1, len(n_str)))


assert is_modest(2036) == True 
assert is_modest(3412) == False
assert is_modest(21333) == True
assert is_modest(8) == False 
assert is_modest(13) == True
assert is_modest(329) == False
assert is_modest(433) == True
assert is_modest(2037) == True
assert is_modest(2038) == False
assert is_modest(12036) == True
assert is_modest(20010) == False
assert is_modest(450810) == True
assert is_modest(4221344) == False
assert is_modest(9111111) == True

print('Success')