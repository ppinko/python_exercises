"""
https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem
"""

a = [1, 2, 3, 4, 5]
d = 4

def rotLeft(a, d):
    a_str = list(map(str, a))
    if d == 0 or d == len(a_str):
        return "".join(a_str)
    else:
        ans = a_str[d:] + a_str[:d]
        return "".join(ans)

print(rotLeft(a, d))

# Alternative solution

# def array_left_rotation(a, n, k):
#     return a[k:]+a[:k]

# n, k = map(int, input().strip().split(' '))
# a = list(map(int, input().strip().split(' ')))
# answer = array_left_rotation(a, n, k);
# print(*answer, sep=' ')