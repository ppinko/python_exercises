"""
https://edabit.com/challenge/9TkNRu9ALS6DAy8jK
"""


from collections import Counter


def highest_occurrence(lst: list) -> list:
    L = [k for k, v in Counter(lst).items() if v == max(Counter(lst).values())]
    A, B = list(), list()
    for i in L:
        if type(i) == int:
            A.append(i)
        else:
            B.append(i)
    A.sort()
    B.sort()
    A.extend(B)
    return A


assert highest_occurrence(["a"]) == ["a"]
assert highest_occurrence(["a","a"]) == ["a"]
assert highest_occurrence(["a","a","b"]) == ["a"]
assert highest_occurrence(["a","a","b"]) == ["a"]
assert highest_occurrence(["a","a","b","b"]) == ["a","b"]
assert highest_occurrence([1,"a","b","b"]) == ["b"]
assert highest_occurrence([1,2,2,3,3,3,4,4,4,4]) == [4]
assert highest_occurrence(["ab","ab","b"]) == ["ab"]
assert highest_occurrence(["ab","ab","b","bb","b"]) == ["ab","b"]
assert highest_occurrence([3,3,3,4,4,4,4,2,3,6,7,6,7,6,7,6,"a","a","a","a"]) == [3,4,6,"a"]
assert highest_occurrence([2,2,"2","2",4,4]) == [2,4,"2"]

print('Success')