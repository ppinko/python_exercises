"""
https://edabit.com/challenge/NQToxLLFCjugHWBoZ

sort_by_character(["az16", "by35", "cx24"], 2) ➞ ["cx24", "by35", "az16"]
// By 2nd character: ["x", "y", "z"] is in alphabetical order.

sort_by_character(["mayor", "apple", "petal"], 5) ➞ ["apple", "petal", "mayor"]
# By 5th character: ["e", "l", "r"] is in alphabetical order

sort_by_character(["mate", "team", "bade"], 3) ➞ ["team", "bade", "mate"]
"""

def sort_by_character(lst, n):
    return sorted(lst, key = lambda x: x[n-1])

print(sort_by_character(["mate", "team", "bade"], 3))
