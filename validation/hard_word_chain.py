"""
https://edabit.com/challenge/SmM8CSnsTTEF3mhX3
"""


def is_word_chain(words):
    if not all(True if len(i) == len(words[0]) else False for i in words):
        return False
    for i in range(1, len(words)):
        tot = 0
        for j, v in enumerate(words[i]):
            if v != words[i-1][j]:
                tot += 1
        if tot > 1:
            return False
    return True


assert is_word_chain(['meal', 'seal', 'seat', 'beat', 'beet']) == True
assert is_word_chain(['red', 'bed', 'bet', 'bat', 'sat']) == True
assert is_word_chain(['heady', 'ready', 'beady', 'beads', 'meads', 'meats', 'seats', 'feats']) == True
assert is_word_chain(['score', 'scare', 'stare', 'spare', 'spire']) == True
assert is_word_chain(['more', 'mire', 'dire', 'dare', 'date']) == True
assert is_word_chain(['read', 'red', 'led', 'lad', 'lady']) == False
assert is_word_chain(['red', 'bat', 'cat', 'sat']) == False
assert is_word_chain(['candy', 'candies', 'fat', 'rat']) == False

print('Success')