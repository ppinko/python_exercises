"""
https://edabit.com/challenge/tNRvtHKZxvqPRnAeF
"""

def digit_occurrences(start, end, digit):
    count = 0
    for i in range(start, end + 1):
        count += str(i).count(str(digit))
    return count

"""
Alternative solution - using generator
"""
##def digit_occurrences(start, end, digit):
##    return ''.join(str(i) for i in range(start,end+1)).count(str(digit))

print(digit_occurrences(51, 55, 5) == 6)
