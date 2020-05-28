"""
https://edabit.com/challenge/K3bpLf794wSSrHmdc
"""


def string_code(txt: str) -> list:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    words = ''.join(i for i in txt if i.isalpha() or i.isspace())
    words = words.lower().split()
    words_len = [len(i) for i in words]
    vowels_num = []
    for word in words:
        tot = 0
        for char in word:
            if char in vowels:
                tot += 1
        vowels_num.append(tot)
    consonants_num = [j - i for i, j in zip(vowels_num, words_len)]
    consonants_str = ' '.join(str(i) for i in consonants_num)
    vowels_str = ' '.join(str(i) for i in vowels_num)
    return [consonants_str, vowels_str]


print(string_code("I'd like to drink my first glass of champagne."))
assert string_code("I'd like to drink my first glass of champagne.") == ['1 2 1 4 2 4 4 1 6', '1 2 1 1 0 1 1 1 3']
assert string_code("The first man to walk on the moon was Neil Armstrong.") == [ '2 4 2 1 3 1 2 2 2 2 7', '1 1 1 1 1 1 1 2 1 2 2']
assert string_code("I've got a lovely bunch of coconuts.") == [ '1 2 0 4 4 1 5', '2 1 1 2 1 1 3' ]
assert string_code("There they are a'standing in a row.") == [ '3 3 1 6 1 0 2', '2 1 2 3 1 1 1' ]
assert string_code("Let them eat cake.") == [ '2 3 1 2', '1 1 2 2' ]
assert string_code("It does not matter how slowly you go as long as you do not stop.") == [ '1 2 2 4 2 5 1 1 1 3 1 1 1 2 3', '1 2 1 2 1 1 2 1 1 1 1 2 1 1 1']
assert string_code("To be or not to be, that is the question.") == [ '1 1 1 2 1 1 3 1 2 4', '1 1 1 1 1 1 1 1 1 4' ]
assert string_code("Believe you can and you're halfway there.") == [ '3 1 2 2 2 5 3', '4 2 1 1 3 2 2' ]

print('Success')