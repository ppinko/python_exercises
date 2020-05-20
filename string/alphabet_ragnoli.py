"""
https://www.hackerrank.com/challenges/alphabet-rangoli/problem

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
"""

import string
n = int( input() )
width = 2 * (n + n - 1) - 1
ls = []
for i in range(n):
    temp_str = string.ascii_lowercase[i:n]
    temp_2 = temp_str[:]
    for i in range(1, len(temp_str)):
        temp_2 = temp_str[i] + temp_2
    temp_3 = []
    for i in temp_2:
        temp_3.append(i)
    temp_4 = "-".join(temp_3)
    ls.append(temp_4)
ls_2 = ls[:]
ls_2.reverse()
ls_2.pop()
ls_2.extend(ls) 
for row in ls_2:
    print(row.center(width, "-"))