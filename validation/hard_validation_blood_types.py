"""
https://edabit.com/challenge/iasdc3ihqt9hkZWfi
"""


def can_give_blood(donor, receiver) -> bool:
    if '+' in donor and '+' not in receiver:
        return False
    elif donor[:-1] in receiver or 'O' in donor:
        return True
    else:
        return False


tests = [
    (("O+", "A+"), True),
    (("A-", "B-"), False),
    (("A-", "AB+"), True),
    (("AB-", "B-"), False),
    (("AB+", "A+"), False),
    (("O-", "A-"), True),
    (("A-", "O-"), False),
    (("O+", "AB-"), False),
    (("O-", "AB+"), True),
    (("AB+", "AB+"), True),
    (("O+", "O-"), False),
]

for test in tests:
    print("Input: " + str(test[0]))
    assert can_give_blood(*test[0]) == test[1]

print('Success')