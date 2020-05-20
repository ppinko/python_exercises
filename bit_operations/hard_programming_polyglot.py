"""
https://edabit.com/challenge/94DMDTYe89i6TLCZh
"""


def get_languages(n: int) -> list:
    lang = ['C#', 'C++', 'Java', 'JavaScript', 'PHP', 'Python', 'Ruby', 'Swift']
    n_bin = bin(n)[2:][::-1]
    return [lang[i] for i, v in enumerate(n_bin) if v == '1']


assert get_languages(32) == ['Python']
assert get_languages(25) == ['C#','JavaScript','PHP']
assert get_languages(100) == ['Java','Python','Ruby']
assert get_languages(255) == ['C#','C++','Java','JavaScript','PHP','Python','Ruby','Swift']
assert get_languages(53) == ['C#','Java','PHP','Python']
assert get_languages(12) == ['Java','JavaScript']

print('Success')

