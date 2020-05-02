"""
https://edabit.com/challenge/xekTcdZjaRMzvvova
"""


def can_build(word: str, lst: list) -> bool:
    temp = []
    for i in word:
        try:
            lst.remove(i.upper())
        except ValueError:
            temp.append(i)
    return lst.count('#') >= len(temp)


assert can_build("quavers", ["S", "U", "Q", "V", "A", "#", "#"]) == True
assert can_build("move", ["M", "U", "T", "V", "E", "J", "#"]) == True
assert can_build("banter", ["N", "E", "B", "N", "#", "A", "T"]) == True
assert can_build("snake", ["S", "K", "E", "N", "V", "J", "A"]) == True
assert can_build("move", ["M", "U", "T", "V", "E", "J", "S"]) == False
assert can_build("sharp", ["S", "K", "H", "#", "#", "F", "F"]) == False
assert can_build("more", ["M", "R", "I", "E", "U", "S", "F"]) == False
assert can_build("talker", ["#", "#", "Z", "V", "P", "A", "K"]) == False
assert can_build("talker", ["#", "#", "T", "T", "A", "A", "L"]) == False
assert can_build("brain", ["#", "S", "B", "B", "I", "I", "#"]) == False
assert can_build("pip", ["#", "P", "I", "S", "V", "W", "Z"]) == True
assert can_build("pip", ["X", "P", "I", "S", "V", "W", "Z"]) == False
assert can_build("stuff", ["F", "F", "X", "S", "U", "A", "T"]) == True
assert can_build("stuff", ["F", "Z", "X", "S", "U", "A", "T"]) == False

print('Success')