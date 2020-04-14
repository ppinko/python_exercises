"""
https://edabit.com/challenge/HrQoXJYqpYZ2Rqvtb
"""

def sum_dig_prod(*args) -> int:
    temp = sum(args)
    if temp < 10:
        return temp
    while temp > 9:
        tot = 1
        while temp > 0:
            tot *= temp % 10
            temp = temp // 10
        temp = tot
        if temp < 10:
            return temp

assert sum_dig_prod(8, 16, 89, 3) == 6
assert sum_dig_prod(16, 28) == 6
assert sum_dig_prod(9) == 9
assert sum_dig_prod(26, 497, 62, 841) == 6

print("Success")
