"""
https://www.hackerrank.com/challenges/kangaroo/problem
"""

def kangaroos(arr):
    a = arr[0]
    x1 = arr[1]
    b = arr[2]
    x2 = arr[3]
    # a + n * x1 = b + n * x2
    if x1 == x2 and a == b:
        print('YES')
    elif x1 == x2:
        print('NO')

    n = (a - b)/(x2 - x1)
    if n <=0:
        print('NO')
    elif n == int(n):
        print('YES')
    else:
        print('NO')

ls_input = [21, 6, 47, 3]
kangaroos(ls_input)