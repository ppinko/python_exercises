"""
https://edabit.com/challenge/oaN8o42vuzsdnCf4x
"""


import string


def best_words(lst: list) -> list:
    points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 2, \
              3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
    d_scra = dict(zip(string.ascii_lowercase, points))
    ans, max_word = [], 0
    for i in lst:
        temp = 0
        for j in i:
            temp += d_scra[j]
        if temp == max_word:
            ans.append(i)
        elif temp > max_word:
            ans.clear()
            ans.append(i)
            max_word = temp
    return ans


assert best_words(['got','test','oh','sat','rents']) == ['oh','rents']
assert best_words(['digest','divest','verge','honey','money']) == ['honey']
assert best_words(['wig','jury','interim','size','hunter']) == ['jury']
assert best_words(['berry','whiz','laughed','ghetto','psychic']) == ['whiz', 'psychic']
assert best_words(['library','index','memory','ghosts','quit']) == ['library','index','memory','quit']
assert best_words(['singing','swine','llamas','crunchy','creamy']) == ['crunchy']

print('Success')