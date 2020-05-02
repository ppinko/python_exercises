"""
https://edabit.com/challenge/4AtqpqKdXAFofa566
"""


def remove_leading_trailing(num: str) -> str:
    if len(set(num)) == 1 and '0' in num:
        return '0'
    elif len(set(num)) == 2 and '0' in num and '.' in num:
        return '0'
    temp = list(num)
    if '.' in num:
        for i in range(len(num) - 1, num.index('.') - 1, -1):
            if num[i] == '0' or num[i] == '.':
                temp.pop()
            else:
                break
    while temp[0] == '0':
        if temp[1] == '.':
            break
        temp.pop(0)
    return ''.join(temp)


""" Alternative solution """


def remove_leading_trailing(n):
    s = str(float(n))
    return s[:-2] if s.endswith('.0') else s


assert remove_leading_trailing("230.000") == "230"
assert remove_leading_trailing("00402") == "402"
assert remove_leading_trailing("03.1400") == "3.14"
assert remove_leading_trailing("30") == "30"
assert remove_leading_trailing("30.0000") == "30"
assert remove_leading_trailing("24340") == "24340"
assert remove_leading_trailing("0404040") == "404040"
assert remove_leading_trailing("0") == "0"
assert remove_leading_trailing("00") == "0"
assert remove_leading_trailing("0.000000") == "0"
assert remove_leading_trailing("0000.000") == "0"
assert remove_leading_trailing("00.0001") == "0.0001"
assert remove_leading_trailing("10000") == "10000"
assert remove_leading_trailing("1345") == "1345"
assert remove_leading_trailing("30.000020") == "30.00002"
assert remove_leading_trailing("00200.1900001") == "200.1900001"

print('Success')