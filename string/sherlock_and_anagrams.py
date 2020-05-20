"""
https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem

Two strings are anagrams of each other if the letters of one 
string can be rearranged to form the other string. Given a 
string, find the number of pairs of substrings of the string 
that are anagrams of each other. 
"""

def anagram(s):
    dictA = {}
    for i in s:
        dictA[i] = dictA.get(i, 0) + 1
    for key in dictA:
        if dictA[key] < 2:
            del dictA[key]
    new_s = 0
    for i in s:
        if i in dictA:
            new_s += i
    