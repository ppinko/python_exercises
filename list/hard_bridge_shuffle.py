"""
https://edabit.com/challenge/nm8zFcqcQ9Rzu45Fm
"""


def bridge_shuffle(l1, l2):
    ans = []
    for i in range(max(len(l1), len(l2))):
        if i < len(l1):
            ans.append(l1[i])
        if i < len(l2):
            ans.append(l2[i])
    return ans


assert bridge_shuffle(['A', 'A', 'A'], ['B', 'B', 'B']) == ['A', 'B', 'A', 'B', 'A', 'B']
assert bridge_shuffle(['C', 'C', 'C', 'C'], ['D']) == ['C', 'D', 'C', 'C', 'C']
assert bridge_shuffle([1, 3, 5, 7], [2, 4, 6]) == [1, 2, 3, 4, 5, 6, 7]
assert bridge_shuffle([10, 9, 8], [1, 2, 3, 4]) == [10, 1, 9, 2, 8, 3, 4]
assert bridge_shuffle(['h', 'h', 'h'], ['a', 'a', 'a']) == ['h', 'a', 'h', 'a', 'h', 'a']

print('Success')