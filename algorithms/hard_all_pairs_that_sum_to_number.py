"""
https://edabit.com/challenge/8LZdBwmpBiLJ5Sobt
"""


def all_pairs(lst: list, num: int) -> list:
    lst.sort()
    ans = []
    for i, v in enumerate(lst[:-1]):
        for j in lst[i+1:]:
            if v + j == num:
                ans.append([v, j])
    return ans



assert all_pairs([2, 4, 5, 3], 7) == [[2, 5], [3, 4]]
assert all_pairs([5, 3, 9, 2, 1], 3) == [[1, 2]]
assert all_pairs([4, 5, 1, 3, 6, 8], 9) == [[1, 8], [3, 6], [4, 5]]
assert all_pairs([5, 2], 14) == []
assert all_pairs([5, 5, 2], 14) == []
assert all_pairs([8, 7, 7, 2, 4, 6], 14) == [[6, 8], [7, 7]]
assert all_pairs([8, 7, 2, 4, 6], 14) == [[6, 8]]
assert all_pairs([1, 3, 5, 4, 0], 4) == [[0, 4], [1, 3]]
assert all_pairs([1, 3, 5, 4, 0, 2], 4) == [[0, 4], [1, 3]]
assert all_pairs([1, 3, 5, 4, 0, 2, 2], 4) == [[0, 4], [1, 3], [2, 2]]

print('Success')