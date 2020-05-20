"""
https://www.geeksforgeeks.org/maximum-product-cutting-dp-36/

Given a rope of length n meters, cut the rope in different parts of integer
lengths in a way that maximizes product of lengths of all parts. You must
make at least one cut. Assume that the length of rope is more than 2 meters.

Examples:

Input: n = 2
Output: 1 (Maximum obtainable product is 1*1)

Input: n = 3
Output: 2 (Maximum obtainable product is 1*2)

Input: n = 4
Output: 4 (Maximum obtainable product is 2*2)

Input: n = 5
Output: 6 (Maximum obtainable product is 2*3)

Input: n = 10
Output: 36 (Maximum obtainable product is 3*3*4)
"""


def max_product_cutting(n: int) -> int:
    d_instant = {2:1, 3:2, 4:4}
    if n in d_instant:
        return d_instant[n]
    d_sub = {2:2, 3:3, 4:4}
    total = 1
    while n not in d_sub:
        total *= 3
        n -= 3
    return total * d_sub[n]


print(max_product_cutting(2))
print(max_product_cutting(3))
print(max_product_cutting(4))
print(max_product_cutting(5))
print(max_product_cutting(10))