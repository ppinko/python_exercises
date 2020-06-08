"""
https://edabit.com/challenge/9WZcCNNCbaLvmHR3P
"""


def is_new(n: int) -> bool:
    n_str = str(n)
    if n < 10:
        return True
    elif '0' not in n_str:
        return n_str == ''.join(sorted(n_str))
    else:
        zeros = n_str.count('0')
        if n_str[1: 1+zeros] != '0' * zeros:
            return False
        without_zeros = n_str.replace('0', '')
        return without_zeros == ''.join(sorted(without_zeros))


assert is_new(0) == True
assert is_new(90) == True
assert is_new(601) == False 
assert is_new(123) == True
assert is_new(321) == False
assert is_new(40567) == True
assert is_new(10783) == False
assert is_new(4444) == True
assert is_new(102) == True
assert is_new(30004) == True
assert is_new(40003) == False
assert is_new(125609) == False
assert is_new(23401) == False

print("Success")