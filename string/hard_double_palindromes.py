"""
https://edabit.com/challenge/kjQGrpw9gfhMhPMF4
"""


def palindrome_set(lst: list) -> list:
    d = []
    for i in lst:
        tot, let, dig = 0, '', ''
        for j in i:
            if j.isalpha():
                let += j
            else:
                dig += j
        if let == let[::-1] and len(let) > 0:
            tot += 1
        if dig == dig[::-1] and len(dig) > 0:
            tot += 1
        d.append(tot)
    return d


assert palindrome_set(["cb77c", "ccc888", "ccc789", "abc89"]) == [2, 2, 1, 0]
assert palindrome_set(["18a99b89cc881ba", "p7o8p987", "p7o", "p7o8"]) == [1, 2, 1, 0]
assert palindrome_set(["ab9a", "abba", "aa78bb8bbaa7", "a88a"]) == [2, 1, 2, 2]
assert palindrome_set(["789", "555", "ccc", "abba"]) == [0, 1, 1, 1]
assert palindrome_set(["7a", "5f", "6c"]) == [2, 2, 2]
assert palindrome_set(["7ab", "5fc", "6cd"]) == [1, 1, 1]
assert palindrome_set(["87ab", "15fc", "26cd"]) == [0, 0, 0]
assert palindrome_set(["1234ab", "144a441"]) == [0, 2]
assert palindrome_set([""]) == [0]

print('Success')