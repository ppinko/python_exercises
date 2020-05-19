"""
https://edabit.com/challenge/4Pe4nySfRnWPCjEwr
"""


def is_stretched(stretched: str, original: str) -> bool:
    if set(stretched) != set(original):
        return False
    import itertools
    L1 = [(key, len(list(group))) for key, group in itertools.groupby(stretched)]
    L2 = [(key, len(list(group))) for key, group in itertools.groupby(original)]
    if len(L1) != len(L2):
        return False
    k = L1[0][1] / L2[0][1]
    for i in range(len(L1)):
        if L1[i][0] != L2[i][0] or L1[i][1] / L2[i][1] != k:
            return False
    return True


assert is_stretched("pppaaannndddaaa", "panda") == True
assert is_stretched("hheelllloo", "hello") == True
assert is_stretched("magnet", "magnet") == True
assert is_stretched("eeeeemmmmmoooootttttiiiiiooooonnnnn", "emotion") == True
assert is_stretched("sssshhiipp", "ship") == False
assert is_stretched("cccaaannnddooorrr", "candor") == False
assert is_stretched("relationshiipp", "relationship") == False
assert is_stretched("magneto", "magnet") == False
assert is_stretched("maggnet", "magnet") == False

print('Success')