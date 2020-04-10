"""
https://edabit.com/challenge/f9yjvFSp3HQC6kQxz
"""

def alt_semi(n):
    temp = n
    semi = 1
    while n > 0:
        semi *= n
        n -= 2
        
    d_fact = {1 : 1}
    for i in range(2, temp + 1):
        d_fact[i] = i * d_fact[i-1]
        
    alt = 0
    flag = True
    while temp > 0:
        if flag:
            alt += d_fact[temp]
            flag = False
        else:
            alt -= d_fact[temp]
            flag = True
        temp -= 1
    return alt - semi

print(alt_semi(3) == 2)
