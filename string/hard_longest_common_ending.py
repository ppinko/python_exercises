"""
https://edabit.com/challenge/SeShBxdG2rhGf4Y5L
"""


def longest_common_ending(w1, w2):
    ans = []
    for i in range(1, min(len(w1), len(w2)) + 1):
        if w1[-i] == w2[-i]:
            ans.append(w1[-i])
        else:
            break
    return ''.join(list(reversed(ans)))


assert longest_common_ending("pitiful", "beautiful") == "tiful"
assert longest_common_ending("truck", "trick") == "ck"
assert longest_common_ending("vote", "asymptote") == "ote"
assert longest_common_ending("multiplication", "ration") == "ation"
assert longest_common_ending("potent", "tent") == "tent"
assert longest_common_ending("skyscraper", "carnivore") == ""

print('Success')