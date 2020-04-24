"""
https://edabit.com/challenge/cvA35yPFAggr7rtve
"""


def directories(dic, main):
    L = [main]
    temp_main = main
    while True:
        for k, v in dic.items():
            if temp_main in v:
                L.append(k)
                temp_main = k
                break
        else:
            break
    return L


def last_ancestor(dic, first, second):
    l_first, l_second = directories(dic, first), directories(dic, second)
    for i in l_first:
        if i in l_second:
            return i


assert last_ancestor({'A':['B', 'C', 'D'], 'B':['E', 'F'], 'D':['G', 'H'], 'G':['I', 'J'], 'H': ['K']}, 'B', 'C') == 'A'
assert last_ancestor({'A':['B', 'C', 'D'], 'B':['E', 'F'], 'D':['G', 'H'], 'G':['I', 'J'], 'H': ['K']}, 'I', 'J') == 'G'
assert last_ancestor({'A':['B', 'C', 'D'], 'B':['E', 'F'], 'D':['G', 'H'], 'G':['I', 'J'], 'H': ['K']}, 'I', 'K') == 'D'
print('Success')