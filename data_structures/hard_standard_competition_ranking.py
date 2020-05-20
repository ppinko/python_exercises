"""
https://edabit.com/challenge/2hk7hFz6haBahtnof
"""


def competition_rank(results, person):
    return sorted(results.values(), reverse=True).index(results[person]) + 1


assert competition_rank({'Aria': 90, 'Brooke': 90, 'Olivia': 90, 'Eve': 74, 'Ellie': 87}, "Ellie") == 4
assert competition_rank({'Ryan': 97, 'Thomas': 85, 'Kai': 95, 'Aiden': 87, 'Logan': 90}, "Logan") == 3
assert competition_rank({'Lilly': 91, 'Harris': 87, 'Archie': 93, 'Lexi': 100, 'Ava': 88}, "Lilly") == 3
assert competition_rank({'Jayden': 90, 'Josh': 90, 'Rebecca': 96, 'Jack': 89, 'Max': 96}, "Rebecca") == 1
assert competition_rank({'Ben': 78, 'Quinn': 84, 'Lena': 84, 'Isla': 92, 'Kayla': 72}, "Ben") == 4

print('Success')