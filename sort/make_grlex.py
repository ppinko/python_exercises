"""
https://edabit.com/challenge/qLMZ2hEvrhRSSSnQw

["small", "big"] ➞ ["big", "small"]
["cat", "ran", "for", "the", "rat"] ➞ ["cat", "for", "ran", "rat", "the"]
["this", "is", "a", "small", "test"] ➞ ["a", "is", "test", "this", "small"]
"""


def make_grlex(lst):
    L = sorted(lst, key=str.__gt__)
    return L


K = ["this", "is", "a", "small", "test"]
make_grlex(K)
