"""
https://edabit.com/challenge/CdcS3feCCEHxtDr2a
"""


def clear_ordering(orders: list) -> bool:
    s1, s2 = set(), set()
    for i in orders:
        s1.add(i[0])
        s2.add(i[1])
    return len(s1) == len(s2) and len(s1.intersection(s2)) == len(s2) - 1


assert clear_ordering([["D", "A"], ["C", "B"], ["A", "C"]]) == True
assert clear_ordering([["D", "A"], ["B", "A"], ["C", "D"]]) == False
assert clear_ordering([["S", "T"], ["T", "U"], ["U", "V"]]) == True
assert clear_ordering([["T", "S"], ["T", "U"], ["U", "V"], ["V", "W"]]) == False
assert clear_ordering([["A", "D"], ["C", "D"]]) == False
assert clear_ordering([["A", "D"], ["D", "C"]]) == True
assert clear_ordering([["c", "d"], ["a", "b"], ["b", "c"]]) == True
assert clear_ordering([["d", "c"], ["a", "b"], ["b", "c"]]) == False
assert clear_ordering([["a", "b"], ["b", "c"], ["c", "d"], ["e", "f"], ["d", "e"]]) == True
assert clear_ordering([["b", "a"], ["b", "c"], ["c", "d"], ["e", "f"], ["d", "e"]]) == False

print("Success")