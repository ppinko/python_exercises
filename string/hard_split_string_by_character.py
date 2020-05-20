"""
https://edabit.com/challenge/D9RrvPomL2JeGXm3q
"""


def split_groups(txt: str) -> list:
    import itertools
    return [key * len(list(group)) for key, group in itertools.groupby(txt)]


assert split_groups('aaabbbaabbab') == ['aaa', 'bbb', 'aa', 'bb', 'a', 'b']
assert split_groups('5556667788') == ['555', '666', '77', '88']
assert split_groups('abbbcc88999&&!!!_') == ['a', 'bbb', 'cc', '88', '999', '&&', '!!!', '_']
assert split_groups('555') == ['555']
assert split_groups('AABBCC') == ['AA', 'BB', 'CC']

print('Success')