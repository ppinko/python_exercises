"""
https://edabit.com/challenge/xng23q8WgoRFNnZM4
"""


def word_groups(lst: list) -> dict:
    L = sorted(lst, key=lambda x: len(x))
    d = dict()
    for i in range(0, len(L) - 1):
        for j in range(i+1, len(L)):
            if L[i] in L[j]:
                if L[i] not in d:
                    d[L[i]] = [L[j]]
                else:
                    d[L[i]].append(L[j])
    for k, v in d.items():
        d[k] = sorted(v)
    return d


assert word_groups(['eve', 'even', 'events', 'level', 'vent']) == {'vent': ['events'], 'even': ['events'], 'eve': ['even', 'events', 'level']}
assert word_groups(['air', 'dairy', 'despair', 'fair', 'lair', 'pair']) == {'air': ['dairy', 'despair', 'fair', 'lair', 'pair'], 'pair': ['despair']}
assert word_groups(['ant', 'antelope', 'cantelope', 'install', 'metallic', 'plan', 'plant', 'tall']) == {'tall': ['install', 'metallic'], 'plan': ['plant'], 'ant': ['antelope', 'cantelope', 'plant'], 'antelope': ['cantelope']}
assert word_groups(['her', 'the', 'here', 'other', 'there']) == {'the': ['other', 'there'], 'here': ['there'], 'her': ['here', 'other', 'there']}
assert word_groups(['pro', 'protect', 'protein', 'enlighten', 'rot', 'rotten', 'ten']) == {'rot': ['protect', 'protein', 'rotten'], 'pro': ['protect', 'protein'], 'ten': ['enlighten', 'rotten']}
assert word_groups(['dice', 'ice', 'iced', 'indices', 'voice']) == {'dice': ['indices'], 'ice': ['dice', 'iced', 'indices', 'voice']}
assert word_groups(['anthem', 'rant', 'rest', 'restaurant', 'them', 'theme', 'ant']) == {'them': ['anthem', 'theme'], 'ant': ['anthem', 'rant', 'restaurant'], 'rest': ['restaurant'], 'rant': ['restaurant']}
assert word_groups(['cargo', 'are', 'bar', 'car', 'careful', 'embargo']) == {'bar': ['embargo'], 'car': ['careful', 'cargo'], 'are': ['careful']}

print('Success')