"""
https://edabit.com/challenge/NbZ2cMeEfH3KpQRku
"""


def percentage_happy(lst: list):
    happy = 0
    for i, v in enumerate(lst):
        if i == 0 and v == lst[i+1]:
            happy += 1
        elif i == len(lst) - 1 and v == lst[i-1]:
            happy += 1
        elif i != 0 and i != len(lst) - 1 \
                and (v == lst[i-1] or v == lst[i+1]):
            happy += 1
    return round(happy / len(lst), 1)


assert percentage_happy([0, 1, 0, 1, 0]) == 0
assert percentage_happy([0, 1, 1, 0]) == 0.5
assert percentage_happy([0, 0, 0, 1, 1]) == 1
assert percentage_happy([1, 0, 0, 1, 1]) == 0.8
assert percentage_happy([1, 1, 1, 1, 1]) == 1
assert percentage_happy([1, 1, 0, 0, 1, 1]) == 1
assert percentage_happy([1, 1, 0, 0, 0, 1, 1]) == 1
assert percentage_happy([1, 0, 0, 0, 1]) == 0.6
assert percentage_happy([1, 0, 1, 0, 0, 0]) == 0.5
assert percentage_happy([1, 1]) == 1
assert percentage_happy([1, 0]) == 0

print('Success')