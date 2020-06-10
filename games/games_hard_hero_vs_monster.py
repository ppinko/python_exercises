"""
https://edabit.com/challenge/y3CEwBrJqqkeefgnt
"""


def battle(stats: dict) -> str:
    hero_health, potion_num, monster_health = stats["pHP"], stats["pPOT"], stats["mHP"]
    rounds = 0
    while True:
        def_factor = 1
        rounds += 1
        if hero_health > 10 or potion_num == 0:
            monster_health -= (2 * stats["pATT"] - stats["mDEF"])
            if monster_health <= 0:
                return "Victory in {} rounds".format(rounds)
        else:
            hero_health += 10
            potion_num -= 1
            def_factor = 0.5
        hero_health -= (2 * stats["mATT"] - stats["pDEF"]) * def_factor
        if hero_health <= 0:
            return "Game Over in {} rounds".format(rounds)



assert battle({"pHP": 10, "pATT": 10, "pDEF": 10, "pPOT": 0, "mHP": 20, "mATT": 6, "mDEF": 14}) == "Victory in 4 rounds"
assert battle({"pHP": 10, "pATT": 10, "pDEF": 10, "pPOT": 2, "mHP": 10, "mATT": 8, "mDEF": 14}) == "Victory in 3 rounds"
assert battle({"pHP": 12, "pATT": 7, "pDEF": 6, "pPOT": 2, "mHP": 30, "mATT": 8, "mDEF": 10}) == "Game Over in 5 rounds"
assert battle({"pHP": 100, "pATT": 12, "pDEF": 8, "pPOT": 3, "mHP": 200, "mATT": 14, "mDEF": 8}) == "Game Over in 5 rounds"
assert battle({"pHP": 300, "pATT": 5, "pDEF": 4, "pPOT": 0, "mHP": 120, "mATT": 10, "mDEF": 6}) == "Game Over in 19 rounds"
assert battle({"pHP": 1480, "pATT": 16, "pDEF": 16, "pPOT": 4, "mHP": 860, "mATT": 14, "mDEF": 20}) == "Victory in 72 rounds"
assert battle({"pHP": 230, "pATT": 3, "pDEF": 20, "pPOT": 2, "mHP": 140, "mATT": 12, "mDEF": 4}) == "Game Over in 64 rounds"
assert battle({"pHP": 90, "pATT": 9, "pDEF": 10, "pPOT": 8, "mHP": 300, "mATT": 8, "mDEF": 4}) == "Victory in 29 rounds"

print("Success")