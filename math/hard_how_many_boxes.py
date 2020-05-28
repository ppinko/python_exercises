"""
https://edabit.com/challenge/QdEAMeXNJAivcTMiT
"""


def boxes(weights: list) -> int:
    box_num, box_weight = 1, weights[0]
    for w in weights[1:]:
        if box_weight + w > 10:
            box_num += 1
            box_weight = w
        else:
            box_weight += w
    return box_num


assert boxes([7, 1, 2, 6, 1, 2, 3, 5, 9, 2, 1, 2, 5]) == 5
assert boxes([2, 7, 1, 3, 3, 4, 7, 4, 1, 8, 2]) == 5
assert boxes([1, 3, 3, 3, 2, 1, 1, 9, 7, 10, 8, 6, 1, 2, 9]) == 8
assert boxes([4, 1, 2, 3, 5, 5, 1, 9]) == 3
assert boxes([3, 1, 2, 7, 2, 6, 1]) == 3
assert boxes([4, 6, 1, 9, 6, 1, 1, 9, 2, 9]) == 6
assert boxes([2, 2, 10, 10, 1, 5, 2]) == 4
assert boxes([9, 6, 2, 3, 1, 2, 4, 8, 3, 1, 3]) == 5
assert boxes([2, 5, 1, 6, 2, 9, 5, 2, 1, 6, 1, 6, 6, 1]) == 7
assert boxes([1, 2, 3, 2, 6, 4, 1]) == 3

print('Success')