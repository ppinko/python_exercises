"""
https://edabit.com/challenge/w53kCGX4JSpH8py9o
"""


def word_game(first, second):
    s, ans = set(), list()
    j = 0
    for i, v in zip(first, second):
        if j == 0:
            j += 1
            s.add(i)
            ans.append(i)
        else:
            if i in s or i[0] != ans[-1][-1]:
                return "Player 2 wins!"
            else:
                s.add(i)
                ans.append(i)

        if v in s or v[0] != ans[-1][-1]:
            return "Player 1 wins!"
        else:
            s.add(v)
            ans.append(v)
    return "Game continues..."


assert word_game(["edabit", "yellow", "growing"], ["tangy", "wedding", "ground"]) == "Game continues..."
assert word_game(["edabit", "yellow", "rowing"], ["tangy", "wedding", "ground"]) == "Player 2 wins!"
assert word_game(["edabit", "yellow", "growing"], ["tangy", "wedding", "round"]) == "Player 1 wins!"
assert word_game(["edabit", "yellow", "growing", "dart"], ["tangy", "wedding", "ground", "tangy"]) == "Player 1 wins!"
assert word_game(["edabit", "yellow", "growing", "dart", "tangy"], ["tangy", "wedding", "ground", "toast", "yellow"]) == "Player 2 wins!"

print('Success')