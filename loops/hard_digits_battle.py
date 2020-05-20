"""
https://edabit.com/challenge/cGB2rkiLYC8jdWn8P
"""


def battle_outcome(n: int) -> int:
    k = str(n)
    new = ''.join(max(k[2*i], k[2*i+1]) for i in range(len(k) // 2) if k[2*i] != k[2*i+1])
    if len(k) % 2 == 1:
        return int(new + k[-1])
    else:
        return int(new)


assert battle_outcome(32531) == 351
assert battle_outcome(111) == 1
assert battle_outcome(5289) == 59
assert battle_outcome(76811) == 781
assert battle_outcome(3245196) == 3596
assert battle_outcome(93552129) == 929

print('Success')