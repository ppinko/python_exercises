"""
https://edabit.com/challenge/7jHaJKK7Yw3SPTJRF
"""


def missing(arr1, arr2):
    for i in arr1:
        try:
            arr2.remove(i)
        except ValueError:
            return i


assert missing([1, 2, 3, 4, 5, 6, 7, 8], [1, 3, 4, 5, 6, 7, 8]) == 2
assert missing(['Jane', 'is', 'pretty', 'ugly'], ['Jane', 'is', 'pretty']) == 'ugly'
assert missing([True, True, False, False, True], [False, True, False, True]) == True
assert missing(['different', 'types', '5', 5, [5], (5,)], ['5', 'different', [5], 'types', 5]) == (5,)
assert missing(list('fate'),list('fat')) == 'e'

print('Success')