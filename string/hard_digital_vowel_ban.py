"""
https://edabit.com/challenge/zwDTaEry2WiY5n4G6
"""

def digital_vowel_ban(num: int, letter: str) -> int:
    d = {0 : 'zero', 1: 'one', 2: 'two', 3:'three', 4:'four',\
         5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
    new_num = ''
    num = str(num)
    for char in num:
        if letter not in d[int(char)]:
            new_num += char
    if len(new_num) == 0:
        return 'Banned Number'
    return int(new_num)

"""
Aleternative solution
"""

def digital_vowel_ban(n, ban):
    d = {'e': '0135789', 'i': '5689', 'o': '0124', 'u': '4'}
    new = ''.join(i for i in str(n) if i not in d.get(ban, ''))
    return 'Banned Number' if not new else int(new)

assert digital_vowel_ban(143, "o") == 3
assert digital_vowel_ban(14266330, "e") == 4266
assert digital_vowel_ban(4020, "u") == 20

print("Success")
