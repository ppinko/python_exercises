"""
https://edabit.com/challenge/vCRP3WXbJ9erKFsiK
"""


def dif_ciph(arg):
    if type(arg) == str:
        return [ord(v) if i == 0 else ord(v) - ord(arg[i-1]) for i, v in enumerate(arg)]
    else:
        ans, k = '', 0
        for i in arg:
            k += i
            ans += chr(k)
        return ans


assert dif_ciph("How are you?") == [72, 39, 8, -87, 65, 17, -13, -69, 89, -10, 6, -54]
assert dif_ciph("?") == [63]
assert dif_ciph([84, 20,  -3,  -69,  78,  -9,  4,  -2,  1,  -6,  13,  6,  -3,  1,  -83,  65,  17,  -13,  -69,  83,  1,  -2,  -17,  13,  -7,  -2,  -55,  0 ]) == "The neighbours are strange.."
assert dif_ciph("It's a secret!") == [73, 43, -77, 76, -83, 65, -65, 83, -14, -2, 15, -13, 15, -83 ]
assert dif_ciph([79, -4 ]) == "OK"
assert dif_ciph([84, 27,  -2,  2,  3,  0,  -3,  8,  -75,  -12,  19,  -19,  80,  -3,  -77,  73,  5,  -78,  84,  -12,  -3,  -69,  71,  -6,  17,  -14,  1,  9,  -64 ]) == "Tomorrow, 3 pm in the garden."
assert dif_ciph(dif_ciph("Double test!")) == "Double test!"
assert dif_ciph("Sunshine") == [83, 34, -7, 5, -11, 1, 5, -9]

print('Success')