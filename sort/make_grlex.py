"""
https://edabit.com/challenge/qLMZ2hEvrhRSSSnQw

["small", "big"] ➞ ["big", "small"]
["cat", "ran", "for", "the", "rat"] ➞ ["cat", "for", "ran", "rat", "the"]
["this", "is", "a", "small", "test"] ➞ ["a", "is", "test", "this", "small"]
"""

def make_grlex(lst):
    return sorted(lst, key = str.__gt__)

print(make_grlex(["this", "is", "a", "small", "test"]))
