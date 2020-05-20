"""
https://edabit.com/challenge/joCBaJztZrdxi9HjR
"""


def tp_checker(d: dict) -> str:
    days = int(d["tp"] * 500 / 57 / d["people"])
    if days < 14:
        return "Your TP will only last {0} days, buy more!".format(days)
    else:
        return "Your TP will last {0} days, no need to panic!".format(days)


assert tp_checker({"people": 4, "tp": 1}) == "Your TP will only last 2 days, buy more!"
assert tp_checker({"people": 2, "tp": 4}) == "Your TP will last 17 days, no need to panic!"
assert tp_checker({"people": 3, "tp": 20}) == "Your TP will last 58 days, no need to panic!"
assert tp_checker({"people": 4, "tp": 12}) == "Your TP will last 26 days, no need to panic!"
assert tp_checker({"people": 6, "tp": 8}) == "Your TP will only last 11 days, buy more!"
assert tp_checker({"people": 1, "tp": 1}) == "Your TP will only last 8 days, buy more!"

print('Success')