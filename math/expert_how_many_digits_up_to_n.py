"""
https://edabit.com/challenge/j9zed4GnykS48W6vh

How Many Digits between 1 and N

magine you took all the numbers between 0 and n and concatenated them together into a long string.
How many digits are there between 0 and n? Write a function that can calculate this.

There are 0 digits between 0 and 1, there are 9 digits between 0 and 10 and there are 189 digits
between 0 and 100.
"""

"""
1 - 9 = 1 * 9
10 - 99 = 2 * 90 
100 - 999 = 3 * 900
1000 - 9999 = 4 * 9000
"""


def digits(n: int) -> int:
    if n == 1:
        return 0
    k, tot = len(str(n)), 0
    while k >= 1:
        if k == len(str(n)):
            tot += (n - pow(10, k - 1)) * k
        else:
            tot += pow(10, k - 1) * k * 9
        k -= 1
    return tot


assert digits(1) == 0
assert digits(10) == 9
assert digits(100) == 189
assert digits(2020) == 6969
assert digits(103496754) == 820359675
assert digits(3248979384) == 31378682729
assert digits(122398758003456) == 1724870258940729
assert digits(58473029386609125789) == 1158349476621071404669

print('Success')