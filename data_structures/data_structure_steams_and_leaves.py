"""
https://edabit.com/challenge/sibD9TFg7pmQuzJxW
"""

from operator import itemgetter
from collections import OrderedDict


def stem_plot(nums: list) -> list:
    separated = [(int(str(i)[:-1]), (int(str(i)[-1]))) if len(str(i)) > 1 else (0, i) for i in nums]
    L = sorted(separated, key=itemgetter(0, 1))
    d = OrderedDict()
    for i in L:
        if i[0] not in d:
            d[i[0]] = [str(i[1])]
        else:
            d[i[0]] += [str(i[1])]
    K = ["{0} | {1}".format(k, ' '.join(v)) for k, v in d.items()]
    return K


assert stem_plot([111, 11, 1]) == ["0 | 1", "1 | 1", "11 | 1"]
assert stem_plot([4, 8, 75]) == ["0 | 4 8", "7 | 5"]
assert stem_plot([22, 22, 38, 22, 19]) == ["1 | 9", "2 | 2 2 2", "3 | 8"]
assert stem_plot([1062, 310, 89, 9, 16]) == ["0 | 9", "1 | 6", "8 | 9", "31 | 0", "106 | 2"]
assert stem_plot([48, 125, 48, 48, 20, 21, 22, 125, 48, 20]) == ["2 | 0 0 1 2", "4 | 8 8 8 8", "12 | 5 5"]
assert stem_plot([36, 12, 2, 4, 1062, 1062, 2, 36, 234]) == ["0 | 2 2 4", "1 | 2", "3 | 6 6", "23 | 4", "106 | 2 2"]
assert stem_plot([555, 555, 555, 555]) == ["55 | 5 5 5 5"]
assert stem_plot([10, 20, 30, 1, 2, 3]) == ["0 | 1 2 3", "1 | 0", "2 | 0", "3 | 0"]

print('Success')