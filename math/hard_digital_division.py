"""
https://edabit.com/challenge/NWR5BK4BYqDkumNiB
"""


def digital_division(n: int):
    counter = 0
    if n < 10:
        return 'Perfect'
    k = str(n)
    n_mul = 1
    n_sum = 0
    flag = True
    for i in range(len(k)):
        n_mul *= int(k[i])
        n_sum += int(k[i])
        if int(k[i]) != 0 and n % int(k[i]) != 0:
            flag = False
    if n_mul != 0 and n % n_mul == 0:
        counter += 1
    if n % n_sum == 0:
        counter += 1
    if flag:
        counter += 1
    if counter == 3:
        return 'Perfect'
    elif counter > 0:
        return counter
    else:
        return 'Indivisible'


print(digital_division(1890))
assert digital_division(21) == 1
assert digital_division(128) == 2
assert digital_division(100) == 2
assert digital_division(12) == "Perfect"
assert digital_division(1890) == 1
print('Success')