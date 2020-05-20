"""
We define super digit x of an integer

using the following rules:

Given an integer, we need to find the super digit of the integer.

If x has only 1 digit, then its super digit is x.
Otherwise, the super digit of x is equal to the super digit of 
the sum of the digits of x. 
"""

def superDigit(n, k):
    # base case

    temp = 0
    for i in str(n):
        temp += int(i)
    if temp * k < 10:
        return temp 
    else:
        return superDigit(temp * k, 1)


n1, k1 = 9875, 4
print(superDigit(n1, k1))

n2, k2 = 123, 3
print(superDigit(n2, k2))