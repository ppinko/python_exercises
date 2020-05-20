"""
https://edabit.com/challenge/aQ3mnvDmcaTJfSbZh
"""

def bw_transform(text):
    first_ls = [(text * 2)[i:i+len(text)] for i in range(len(text))]
    return ''.join((i[len(text)-1] for i in sorted(first_ls)))

"""
Alternative solution
"""

def bw_transform(txt):
    rotations = sorted(txt[i:] + txt[:i] for i in range(len(txt)))
    return ''.join(i[-1] for i in rotations)

assert bw_transform("banana$") == "annb$aa"
assert bw_transform("mississippi$") == "ipssm$pissii"
assert bw_transform("abaaba$") == "abba$aa"

print("Success")
