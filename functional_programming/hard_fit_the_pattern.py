"""

"""


def check_pattern(lst, pattern):
    d = {}
    for i in list(zip(pattern, lst)):
        if i[0] in d and d[i[0]] != i[1]:
            return False
        else:
            d[i[0]] = i[1]
    if len(set(list(map(tuple, d.values())))) != len(set(pattern)):
        return False
    return True


assert check_pattern([[1, 1], [2, 2], [1, 1], [2, 2]], "ABAB") == True
assert check_pattern([[1, 2], [1, 2], [1, 2], [1, 2]], "AAAA") == True
assert check_pattern([[1, 2], [1, 3], [1, 4], [1, 2]], "ABCA") == True
assert check_pattern([[1, 2, 3], [1, 2, 3], [3, 2, 1], [3, 2, 1]], "AABB") == True
assert check_pattern([[8, 8, 8, 8], [7, 7, 7, 7], [6, 6, 6, 6], [5, 5, 5, 5]], "ABCD") == True
assert check_pattern([[8, 8, 8, 8], [7, 7, 7, 7], [6, 6, 6, 6], [5, 5, 5, 5]], "DCBA") == True
assert check_pattern([[8], [7], [6], [6]], "ABCC") == True
assert check_pattern([[8], [9], [9], [9]], "ABBB") == True
assert check_pattern([[1, 1], [2, 2], [1, 1], [1, 2]], "ABAB") == False
assert check_pattern([[1, 2], [1, 2], [2, 2], [3, 2]], "AAAA") == False
assert check_pattern([[8], [9], [9], [8]], "ABBB") == False
assert check_pattern([[8], [7], [6], [5]], "ABCC") == False
assert check_pattern([[8, 8, 8, 8], [7, 7, 7, 7], [6, 6, 6, 6], [5, 5, 5, 5]], "DDBA") == False
assert check_pattern([[1, 2], [1, 2], [1, 2], [1, 2]], "AABA") == False

print('Success')