"""
https://www.hackerrank.com/challenges/ctci-ransom-note/problem
"""

def checkMagazine(magazine, note):
    dict_magazine = {}
    for i in magazine:
        dict_magazine[i] = dict_magazine.get(i, 0) + 1
    for j in note:
        dict_magazine[j] = dict_magazine.get(j, -1) - 1
        if dict_magazine[j] < 0:
            return print("No")
    return print("Yes")