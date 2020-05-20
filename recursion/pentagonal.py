"""
https://edabit.com/challenge/st8mDxreMcuWxuz8c
"""

def pentagonal(num):
    if num == 1:
        return 1
    return 5 * (num -1 ) + pentagonal(num - 1)

#### Not a recursive solution

##def pentagonal(num):
##    """Linear solution
##
##    num - int"""
##    count = 1
##    for i in range(1, num+1):
##        count += 5 * (i - 1)
##    return count

print(pentagonal(8) == 141)

