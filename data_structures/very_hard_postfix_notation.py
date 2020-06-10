"""
https://edabit.com/challenge/79tuQhjqs8fT7zKCY
"""


def postfix(expr):
    L = expr.split()
    operators = [i for i in L if not i.isdigit()]
    K = []
    for i, v in enumerate(L):
        if v.isdigit():
            K.append(v)
        elif K[i-1].isdigit() and K[i-2].isdigit():
            K.insert(i-1, v)
        else:
            for j, v2 in enumerate(K):
                if v2.isdigit() and K[j+1].isdigit():
                    K.insert(j + 1, v)
                    break
    for i in operators:
        j = K.index(i)
        middle = K[j-1: j+2]
        del K[j-1: j+2]
        to_insert = str(int(eval(' '.join(middle))))
        K.insert(j-1, to_insert)
    return int(K[0])



assert postfix("2 2 +") == 4
assert postfix("2 3 * 1 - 5 /") == 1
assert postfix("5") == 5
assert postfix("10 10 * 10 /") == 10
print(postfix("5 6 * 2 1 + /"))
assert postfix("5 6 * 2 1 + /") == 10
assert postfix("1 1 + 2 2 + -") == -2
assert postfix("8 4 / 9 * 3 1 * /") == 6

print("Success")