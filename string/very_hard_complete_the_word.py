"""
https://watchtwoandahalfmenonline.com/watch-free/two-and-a-half-men-5x9/#
"""


def can_complete(word: str, txt: str) -> bool:
    index = 0
    for i in word:
        temp = txt[index:].find(i)
        print(temp, txt[index:])
        if temp != -1:
            index += temp + 1
        else:
            return False
    return True


# assert can_complete('butl', 'beautiful') == True
# assert can_complete('butlz', 'beautiful') == False
# assert can_complete('tulb', 'beautiful') == False
# assert can_complete('bbutl', 'beautiful') == False
assert can_complete('siing', 'something') == False
print('Success')