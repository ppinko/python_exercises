"""
https://edabit.com/challenge/9yk63KrKDHzNFWKBJ
"""


def directories(dic, main):
    L = []
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


def is_it_inside(dic, first, second):
    if first == second:
        return True
    return second in directories(dic, first)


assert is_it_inside({'A':['B', 'C', 'D'], 'B':['E', 'F'], 'D':['G', 'H'], 'G':['I', 'J'], 'H': ['K']}, 'B', 'A') == True
assert is_it_inside({'A':['B', 'C', 'D'], 'B':['E', 'F'], 'D':['G', 'H'], 'G':['I', 'J'], 'H': ['K']}, 'B', 'D') == False
assert is_it_inside({'A':['B', 'C', 'D'], 'B':['E', 'F'], 'D':['G', 'H'], 'G':['I', 'J'], 'H': ['K']}, 'I', 'D') == True
print('Success')