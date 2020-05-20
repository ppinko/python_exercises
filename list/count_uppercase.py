"""
https://edabit.com/challenge/Hs7YDjZALCEPRPD6Z
"""

def count_uppercase(lst):
    return sum(1 for row in lst for c in row if c.isupper())

print(count_uppercase(['SOLO', 'hello', 'Tea', 'wHat']))
print(count_uppercase(['SOLO', 'hello', 'Tea', 'wHat']) == 6)
