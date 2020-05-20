"""
https://edabit.com/challenge/uwFHSRewNpmBNvbME
"""


from collections import Counter


def same_vowel_group(lst: list) -> list:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    temp = [frozenset(vowels.intersection(i)) for i in lst]
    c = Counter(temp)
    c_most_common = c.most_common(1)
    if c_most_common[0][1] == 1:
        return [lst[0]]
    return [lst[i] for i, v in enumerate(temp) if v == c_most_common[0][0]]


assert same_vowel_group(["hoops", "chuff", "bot", "bottom"]) == ["hoops", "bot", "bottom"]
assert same_vowel_group(["crop", "nomnom", "bolo", "yodeller"]) == ["crop", "nomnom", "bolo"]
assert same_vowel_group(["semantic", "aimless", "beautiful", "meatless icecream"]) == ["semantic", "aimless", "meatless icecream"]
assert same_vowel_group(["many", "carriage", "emit", "apricot", "animal"]) == ["many"]
assert same_vowel_group(["toe", "ocelot", "maniac"]) == ["toe", "ocelot"]
assert same_vowel_group(["a", "apple", "flat", "map", "shark"]) == ["a", "flat", "map", "shark"]
assert same_vowel_group(["a", "aa", "ab", "abc", "aaac", "abe"]) == ["a", "aa", "ab", "abc", "aaac"]

print('Success')