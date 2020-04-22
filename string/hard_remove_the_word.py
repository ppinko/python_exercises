"""
https://edabit.com/challenge/gH3QMvF3czMDjENkk
"""


def remove_letters(letters, word):
    _ = [letters.remove(i) for i in word if i in letters]
    return letters


assert remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string") == ["w"]
assert remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon") == ["b", "g", "w"]
assert remove_letters(["d", "b", "t", "e", "a", "i"], "edabit") == []
assert remove_letters(["t", "t", "e", "s", "t", "u"], "testing") == ["t", "u"]
print('Success')