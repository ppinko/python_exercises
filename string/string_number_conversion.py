"""
Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
"""

def alg(n):
    return n + 11*n + 111*n + 1111*n

print(alg(9))

def alg2(n):
    base = "a+aa+aaa+aaaa"
    x = base.replace('a', str(n))
    y = x.split('+')
    ans = 0
    for i in y:
        ans += int(i)
    return ans

print(alg2(9))

a = input()
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
n4 = int( "%s%s%s%s" % (a,a,a,a) )
print(n1+n2+n3+n4)