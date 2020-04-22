"""
https://edabit.com/challenge/YjwJ6BfujKtmuTMqW
"""


def dice_game(lst: list) -> str:
    p = ['p1', 'p2', 'p3', 'p4']
    i = 0
    while True:
        temp = [[sum(j), j[0]] for j in lst[i:i+len(p)]]
        i += len(p)
        l = list(zip(*temp))
        x = min(l[0])
        if l[0].count(x) == 1:
            y = l[0].index(x)
            p.pop(y)
        elif l[0].count(x) >= 1:
            z = min(l[1])
            if l[1].count(z) == 1:
                r = l[1].index(z)
                p.pop(r)
        if len(p) == 1:
            return p[0]


assert dice_game([(1, 3), (2, 6), (6, 3), (5, 6), (2, 2), (5, 6), (5, 4), (1, 3), (5, 6)]) == 'p4'
assert dice_game([(4, 4), (4, 3), (1, 1), (1, 1), (3, 1), (4, 5), (2, 6), (2, 3), (1, 5), (5, 3), (4, 5), (5, 2), (2, 1)]) == 'p3'
assert dice_game([(6, 1), (4, 3), (2, 5), (1, 4), (6, 2), (2, 5), (1, 4), (6, 4), (4, 3)]) == 'p1'
print('Success')