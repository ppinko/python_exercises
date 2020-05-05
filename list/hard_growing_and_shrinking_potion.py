"""
https://edabit.com/challenge/FDxu6i6J2GnivsrBq
"""


def after_potion(num: str) -> str:
    ans = ''
    for i, v in enumerate(num):
        if i == len(num) - 1:
            if v.isdigit():
                ans += v
        elif num[i+1] == 'A':
            ans += str(int(v) + 1)
        elif num[i+1] == 'B':
            ans += str(int(v) - 1)
        elif v.isdigit():
            ans += v
        else:
            pass
    return ans


assert after_potion("567") == "567"
assert after_potion("3A78B51") == "47751"
assert after_potion("9999B") == "9998"
assert after_potion("9A123") == "10123"
assert after_potion("1A2A3A4A") == "2345"
assert after_potion("9B8B7B6A") == "8767"

print('Success')