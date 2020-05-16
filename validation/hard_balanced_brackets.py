"""
https://edabit.com/challenge/97Shytt5nzjX4YWzJ
"""



def isBalanced(txt: str):
    if type(txt) != str:
        return None
    d = {']':'[', ')':'(', '}':'{'}
    L = list(txt)

    if txt.count(']') > 0:
        a = txt.find(']')
    else:
        a = 20
    if txt.count(')') > 0:
        b = txt.find(')')
    else:
        b = 20
    if txt.count('}') > 0:
        c = txt.find('}')
    else:
        c = 20

    if a == 20 and b == 20 and c == 20 and len(L) > 0:
        return False

    while len(L) > 0 and ((a > 0 and a != 20) or (b > 0 and b != 20) or (c > 0 and c != 20)):
        print(L)
        x = min(a, b, c)
        if x == 0:
            return False
        elif d[L[x]] == L[x-1]:
            L.pop(x-1)
            L.pop(x-1)
        else:
            return False

        if L.count(']') > 0:
            a = L.index(']')
        else:
            a = 20
        if L.count(')') > 0:
            b = L.index(')')
        else:
            b = 20
        if L.count('}') > 0:
            c = L.index('}')
        else:
            c = 20

        if a == 20 and b == 20 and c == 20 and len(L) > 0:
            return False
    return True


print(isBalanced('{[()]}'))
assert isBalanced('()') == True
assert isBalanced('{[()]}') == True
assert isBalanced('{{[[(())]]}}') == True
assert isBalanced('{{[[(())[]]]}}') == True
assert isBalanced('[()]{}{[()()]()}') == True
assert isBalanced('{[([)]]}') == False
assert isBalanced('{[(') == False
assert isBalanced('])}') == False
assert isBalanced('[[]') == False
assert isBalanced('{)(}') == False
assert isBalanced('{{[[([())]]]}}') == False
assert isBalanced(None) == None

print('Success')