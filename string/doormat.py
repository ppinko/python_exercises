"""
https://www.hackerrank.com/challenges/designer-door-mat/problem

Input: 
9 27

Output:
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
"""

n = input().split()
n = tuple(n)
greeting = "WELCOME"
pattern = '.|.'
mid = int((1 + int(n[0])) / 2)
for i in range(int(n[0])):
    if i < mid - 1:
        print((pattern * (1 + 2 * i)).center(int(n[1]), '-'))
    elif i == mid - 1:
        print(greeting.center(int(n[1]), '-'))
    else:
        print((pattern * (1 + 2 * (int(n[0]) - 1 - i))).center(int(n[1]), '-'))

