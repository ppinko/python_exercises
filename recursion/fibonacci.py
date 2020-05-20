"""
https://edabit.com/challenge/8Ko5tPg8Ch5SRCAhA
"""

def fibonacci(num):
    if num == 0 or num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)    

### Alternative solution

##def fibonacci(num):
##    a, b = 0, 1
##    for _ in range(num):
##        a, b = b, a + b
##    return b

print(fibonacci(12) == 233)
