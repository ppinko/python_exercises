"""
https://edabit.com/challenge/zZyeau2MYcEc8Fdtk
"""

def round_number(n1, n2):
    k = n1 // n2
    v1 = (k+1)*n2-n1
    v2 = n1-k*n2
    if (v1 == v2):
        return (k+1) * n2
    elif v1 < v2:
        return (k+1)*n2
    else:
        return k*n2
        
assert round_number(34, 25) == 25
assert round_number(54, 8) == 56
assert round_number(65, 10) == 70
assert round_number(6247, 163) == 6194

print("Success")
