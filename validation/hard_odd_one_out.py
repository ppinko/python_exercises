"""
https://edabit.com/challenge/gSGzRjyB3vC6bnMaZ
"""


def odd_one_out(lst: list) -> bool:
    from collections import Counter
    c = Counter([len(i) for i in lst])
    if len(c) > 2:
        return False
    for i in c.values():
        if i == 1 or i == len(lst) - 1:
            continue
        else:
            return False
    return True


assert odd_one_out(["silly", "mom", "let", "the"]) == True
assert odd_one_out(["swanky", "rhino", "moment"]) == True
assert odd_one_out(["the", "them", "theme"]) == False
assert odd_one_out(["very", "to", "an", "some"]) == False
assert odd_one_out(["very", "to", "then", "some"]) == True
assert odd_one_out(["ab", "cd", "ef", "gh", "a"]) == True
assert odd_one_out(["abcd", "cdef", "a", "efgh", "ghij"]) == True
assert odd_one_out(["abcd", "cdef", "abc", "def", "efgh", "ghij"]) == False
assert odd_one_out(["def", "abcd", "cdef", "abc", "efgh", "ghij"]) == False
assert odd_one_out(["def", "abcd", "cdef", "efgh", "ghij", "abc"]) == False
assert odd_one_out(["a", "b", "cf", "efg"]) == False

print('Success')