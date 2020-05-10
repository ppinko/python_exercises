"""
https://edabit.com/challenge/C6pHyc4iN6BNzmhsM
"""


from collections import Counter


def poker_hand_ranking(hand: list) -> str:
    rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    card_rank = dict(zip(rank, range(1, 14)))
    cards = [(i[:-1], i[-1]) for i in hand]
    colors = {i[1] for i in cards}
    figures = [i[0] for i in cards]
    figures_rank = sorted(card_rank[i] for i in figures)
    figures_sorted = all(True if figures_rank[i] - figures_rank[i-1] == 1 else False
                         for i in range(1, len(figures_rank)))
    c = Counter(figures)

    if len(colors) == 1 and all(True if i in {'10', 'J', 'Q', 'A', 'K'} else False \
                                for i in figures):
        return "Royal Flush"
    elif len(colors) == 1 and figures_sorted:
        return "Straight Flush"
    elif max(c.values()) == 4:
        return "Four of a Kind"
    elif 2 in c.values() and 3 in c.values():
        return "Full House"
    elif len(colors) == 1:
        return "Flush"
    elif figures_sorted:
        return "Straight"
    elif 3 in c.values():
        return "Three of a Kind"
    elif sorted(c.values()) == [1, 2, 2]:
        return "Two Pair"
    elif 2 in c.values():
        return "Pair"
    else:
        return "High Card"


assert poker_hand_ranking(["10h", "Jh", "Qh", "Ah", "Kh"]) == "Royal Flush"
assert poker_hand_ranking(["3h", "5h", "Qs", "9h", "Ad"]) == "High Card"
assert poker_hand_ranking(["10s", "10c", "8d", "10d", "10h"]) == "Four of a Kind"
assert poker_hand_ranking(["4h", "9s", "2s", "2d", "Ad"]) == "Pair"
assert poker_hand_ranking(["10s", "9s", "8s", "6s", "7s"]) == "Straight Flush"
assert poker_hand_ranking(["10c", "9c", "9s", "10s", "9h"]) == "Full House"
assert poker_hand_ranking(["8h", "2h", "8s", "3s", "3c"]) == "Two Pair"
assert poker_hand_ranking(["Jh", "9h", "7h", "5h", "2h"]) == "Flush"
assert poker_hand_ranking(["Ac", "Qc", "As", "Ah", "2d"]) == "Three of a Kind"
assert poker_hand_ranking(["Ad", "Kd", "Qd", "Jd", "9d"]) == "Flush"
assert poker_hand_ranking(["10h", "Jh", "Qs", "Ks", "Ac"]) == "Straight"
assert poker_hand_ranking(["3h", "8h", "2s", "3s", "3d"]) == "Three of a Kind"
assert poker_hand_ranking(["4h", "Ac", "4s", "4d", "4c"]) == "Four of a Kind"
assert poker_hand_ranking(["3h", "8h", "2s", "3s", "2d"]) == "Two Pair"
assert poker_hand_ranking(["8h", "8s", "As", "Qh", "Kh"]) == "Pair"
assert poker_hand_ranking(["Js", "Qs", "10s", "Ks", "As"]) == "Royal Flush"
assert poker_hand_ranking(["Ah", "3s", "4d", "Js", "Qd"]) == "High Card"

print('Success')