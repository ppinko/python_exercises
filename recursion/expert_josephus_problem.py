"""
https://edabit.com/challenge/Mb8KmicGqpP3zDcQ5
"""


def josephus(num, step):
    if step == 1:
        return num
    ls = [i for i in range(num)]
    counter = 0
    while ls.count('-') < num - 1:
        for i in range(len(ls)):
            if ls[i] != '-' and counter != step - 1:
                counter += 1
            elif ls[i] != '-' and counter == step - 1:
                ls[i] = '-'
                counter = 0
    return list(i for i, v in enumerate(ls) if v != '-')[0] + 1


assert josephus(41, 3) == 31
assert josephus(14, 2) == 13
assert josephus(35, 11) == 18
assert josephus(20, 1) == 20
assert josephus(15, 15) == 4
print('Success')