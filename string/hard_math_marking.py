def left_side(x : str) -> int:
    if x.find('+') != -1:
        i = x.index('+') 
        plus = True
    else:
        i = x.index('-')
        plus = False
    a = int(x[:i])
    b = int(x[i+1:])
    if plus:
        return a + b
    return a - b

def mark_maths(ls : list) -> str:
    k = len(ls)
    tot = 0
    for i in ls:
        p = i.index('=')
        left = left_side(i[:p])
        right = int(i[p+1:])
        if left == right:
            tot += 1
    return "{}%".format(round(100 * tot / k))

"""
Alternative solution
"""

def mark_maths(lst):
	correct = sum(eval(i.replace('=', '==')) for i in lst)
	return '{:.0%}'.format(correct / len(lst))

assert mark_maths(['2+2=4', '3+2=5', '10-3=3', '5+5=10']) == '75%'
assert mark_maths(['1-2=-2']) == '0%'
assert mark_maths(['2+3=5', '4+4=9', '3-1=2']) == '67%'

