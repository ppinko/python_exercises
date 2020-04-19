"""
https://edabit.com/challenge/HSKvp4qYA2AhDWxn6
"""


def total_points(guesses, word):
    points = 0
    d = {}
    for i in word:
        d[i] = d.get(i, 0) + 1
    for guess in guesses:
        flag = True
        g = {}
        for i in guess:
            g[i] = g.get(i, 0) + 1
        for i in g.keys():
            if g[i] > d.get(i, 0):
                flag = False
        if flag:
            points += len(guess) - 2
            if len(guess) == 6:
                points += 50
    return points


assert total_points(["dote", "dotes", "toes", "set", "dot", "dots", "sted"], "tossed") == 13
assert total_points(["dial", "tail", "lid", "tide", "date", "late", "tad"], "detail") == 12
assert total_points(["bluest", "sublet", "let", "set", "belt", "belts", "bet", "bets", "sted", "but", "tule"], "subtle") == 121
print('Success')