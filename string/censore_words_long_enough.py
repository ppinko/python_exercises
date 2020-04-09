"""
https://edabit.com/challenge/jWk79SoDXnfm8ymhw
"""

def censor(s):
    """
    Complexity - O(n)
    """
    ls = s.split(' ')    
    for i in range(len(ls)):
        j = len(ls[i])
        if j > 4:
            ls[i] = '*' * j
    ans = ' '.join(ls)
    return ans

## Alternative solution
##def censor(s):
##	return ' '.join('*'*len(i) if len(i) > 4 else i for i in s.split())

print(censor("The code is fourty") == "The code is ******")
