"""
https://edabit.com/challenge/S9A7PeacnDpvXLgYe
"""


def longest_abecedarian(lst: list) -> str:
    max_word = ''
    for i in lst:
        flag = True
        for j in range(1, len(i)):
            if i[j] < i[j-1]:
                flag = False
                break
        if flag and len(max_word) < len(i):
            max_word = i
    return max_word


assert longest_abecedarian(['ace', 'spades', 'hearts', 'clubs']) == 'ace'
assert longest_abecedarian(['forty', 'choppy', 'ghost']) == 'choppy'
assert longest_abecedarian(['one', 'two', 'three']) == ''
assert longest_abecedarian(['almost', 'accept', 'access']) == 'almost'
assert longest_abecedarian(['aa', 'bbb', 'cccc']) == 'cccc'


print('Success')