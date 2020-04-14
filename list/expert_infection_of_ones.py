"""
https://edabit.com/challenge/tY5fmSbk85N8digXQ
"""

def ones_infection(ls: list) -> list:
    if len(ls) == 1:
        if ls == [[1]] or ls == [[0]]:
            return ls
        elif 1 in ls[0]:
            for i in range(len(ls)):
                ls[0][i] = 1
            return ls
        else:
            return ls

    d = [ str(row) + str(i) for row in range(len(ls)) for i in range(len(ls[0])) \
          if ls[row][i] == 1]
    row = len(ls)
    column = len(ls[0])
    for i in d:
        a, b = int(i[0]), int(i[1])
        for j in range(column):
            ls[a][j] = 1
        for k in range(row):
            ls[k][b] = 1
    return ls

i4 = [
[0, 1, 0, 1, 0], 
[0, 0, 0, 0, 0], 
[0, 1, 1, 1, 0]
]
i5 = [
[1, 0, 1, 0], 
[0, 0, 0, 0], 
[0, 0, 0, 0]
]

assert ones_infection(i4) == [
[1, 1, 1, 1, 1], 
[0, 1, 1, 1, 0], 
[1, 1, 1, 1, 1]]

assert ones_infection(i5) == [
[1, 1, 1, 1], 
[1, 0, 1, 0], 
[1, 0, 1, 0]]

print("Success")
