"""
https://www.geeksforgeeks.org/cutting-a-rod-dp-13/

Given a rod of length n inches and an array of prices that contains prices
of all pieces of size smaller than n. Determine the maximum value
obtainable by cutting up the rod and selling the pieces. For example, if
length of the rod is 8 and the values of different pieces are given as
following, then the maximum obtainable value is 22 (by cutting in two
pieces of lengths 2 and 6)

length   | 1   2   3   4   5   6   7   8
--------------------------------------------
price    | 1   5   8   9  10  17  17  20

And if the prices are as following, then the maximum obtainable value is 24
(by cutting in eight pieces of length 1)

length   | 1   2   3   4   5   6   7   8
--------------------------------------------
price    | 3   5   8   9  10  17  17  20
"""


def rod(lengths, prices, n, k):
    if n == 0 or len(lengths) == 0 or k == 0:
        return 0
    elif lengths[k-1] > n:
        return rod(lengths, prices, n, k-1)
    else:
        return max(rod(lengths, prices, n, k-1),
                   prices[k-1] + rod(lengths, prices, n - lengths[k-1], k))


n = 8
k = 8
lengths = [1, 2, 3, 4, 5, 6, 7, 8]
prices1 = [1, 5, 8, 9, 10, 17, 17, 20]
prices2 = [3, 5, 8, 9, 10, 17, 17, 20]

assert rod(lengths, prices1, n, k) == 22
assert rod(lengths, prices2, n, k) == 24

print('Success')