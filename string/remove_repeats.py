"""
https://edabit.com/challenge/3Eia4oLLCcyyLN2L7
"""

def remove_repeats(s):
    return s[0] + ''.join(s[i] for i in range(1, len(s)) if s[i] != s[i-1])            

print(remove_repeats('bookkeeper'))
print(remove_repeats('bookkeeper') == "bokeper")
