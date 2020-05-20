"""
https://www.hackerrank.com/challenges/py-the-captains-room/problem
"""

def captain(k, l):
    d = {}
    for i in l:
        d[i] = d.get(i,0) + 1
    for k, v in d.items():
        if v == 1:
            print(k)
