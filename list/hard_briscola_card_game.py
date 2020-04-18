"""
https://edabit.com/challenge/vZJJjYWtzYCBEnnGY
"""


def briscola_score(first: list, second: list) -> str:
    points = {'A': 11, '3': 10, 'K': 4, 'Q': 3, 'J': 2}
    total = sum(points[i[0]] for i in (first + second) if i[0] in points)
    if total > 120:
        return "You Win!"
    elif total < 120:
        return "You Lose!"
    else:
        return "Draw!"


assert briscola_score(["3c", "3s", "Qd", "Jh", "5d", "Jc", "6d", "Ad", "Js", "Qc"],
                      ["Jd", "Kd", "4c", "6s", "Ks", "5c", "3d", "As", "Jh", "6h"]) == "You Lose!"
assert briscola_score(["Ac", "As", "3d", "3h", "3s", "Ah", "Kd"], ["3d", "Ad", "Ac", "As", "Ah"]) == "You Win!"
assert briscola_score(["Ac", "As", "3d", "3h", "3s", "Ah", "Kd"], ["3d", "Ad", "Ac", "As", "3h"]) == "Draw!"
print("Succes")
