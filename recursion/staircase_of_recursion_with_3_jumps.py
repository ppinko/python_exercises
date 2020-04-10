"""
https://edabit.com/challenge/9S8qp4XKG2qwQMdrb

Same task as in the link but possible to jump also 3 steps at the time
"""

d = {0:1, 1:1, 2:2}
total = 0

##def ways_to_climb(n):
##    global total
##    total += 1
##    if n < 0:
##        return 0
##    elif n == 0:
##        return 1
##    return ways_to_climb(n-1) + ways_to_climb(n-2) + ways_to_climb(n-3)
##
##print(ways_to_climb(4) == 7)
####ways_to_climb(10)
##print(total) # for 4 is 25

"""
Alternative solution with memoization
"""

##def ways_to_climb(n, d):
##    global total
##    total += 1
##    if n in d:
##        return d[n]
##    else:
##        d[n] = ways_to_climb(n-1, d) + ways_to_climb(n-2, d) + ways_to_climb(n-3, d)
##        return d[n]
##
##print(ways_to_climb(4, d) == 7)
####ways_to_climb(10, d)
##print(d) # for 4 is 7
##print(total)

"""
Alternative solution with memoization using global variable
"""

def ways_to_climb(n):
    global total
    global d
    total += 1
    if n in d:
        return d[n]
    else:
        d[n] = ways_to_climb(n-1) + ways_to_climb(n-2) + ways_to_climb(n-3)
        return d[n]

print(ways_to_climb(4) == 7)
##ways_to_climb(10)
print(d) # for 4 is 7
print(total)
