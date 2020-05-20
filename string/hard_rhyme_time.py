"""
https://edabit.com/challenge/jwiJNMiCW6P5d2XXA
"""


def does_rhyme(first: str, second: str) -> bool:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    ls1 = [i for i in first if i in vowels]
    ls2 = [i for i in second if i in vowels]
    return ls1[-1] == ls2[-1]


print(does_rhyme('Sam I am!', 'Green eggs and ham.'))
assert does_rhyme('Sam I am!', 'Green eggs and ham.') == True
assert does_rhyme('Sam I am!', 'Green eggs and HAM.') == True
assert does_rhyme('head straight to town', 'give me not a frown') == True
print('Success')