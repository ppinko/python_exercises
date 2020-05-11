"""
https://edabit.com/challenge/hv572GaPtbqwhJpTb
"""


def elasticize(txt: str) -> str:
    a, b = '', ''
    if len(txt) % 2 == 0:
        for i, v in enumerate(txt[:len(txt) // 2]):
            a += v * (i+1)
        c = txt[len(txt) // 2:]
        for j, v in enumerate(c[::-1]):
            b += v * (j+1)
    else:
        for i, v in enumerate(txt[:1 + len(txt) // 2]):
            a += v * (i + 1)
        c = txt[1 + len(txt) // 2:]
        for j, v in enumerate(c[::-1]):
            b += v * (j+1)
    b = b[::-1]
    return a + b


assert elasticize("ANNA") == "ANNNNA"
assert elasticize("KAYAK") == "KAAYYYAAK"
assert elasticize("X") == "X"
assert elasticize("ABC") == "ABBC"
assert elasticize("BOB") == "BOOB"
assert elasticize("OTTO") == "OTTTTO"
assert elasticize("LEVEL") == "LEEVVVEEL"
assert elasticize("IJKCBA") == "IJJKKKCCCBBA"
assert elasticize("REDDER") == "REEDDDDDDEER"
assert elasticize("ROTATOR") == "ROOTTTAAAATTTOOR"

print('Success')