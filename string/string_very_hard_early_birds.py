"""
https://edabit.com/challenge/hCAStny5sJwYP3evS
"""


def is_early_bird(limit, n):
    seq = ''.join(str(i) for i in range(limit+1))
    L, n_str, j, l_str = [], str(n), 0, len(str(n))
    while seq.find(n_str, j) != -1:
        temp = []
        start = seq.find(n_str, j)
        for k in range(l_str):
            temp.append(start+k)
        j = start + 1
        L.append(temp)
    if len(L) > 1:
        L.append('Early Bird!')
    return L


assert is_early_bird(20, 12) == [[1, 2], [14, 15], 'Early Bird!']
assert is_early_bird(20, 14) == [[18, 19]]
assert is_early_bird(101, 101) == [[10, 11, 12], [193, 194, 195], 'Early Bird!']
assert is_early_bird(50, 34) == [[3, 4], [58, 59], [77, 78], 'Early Bird!']
assert is_early_bird(212, 156) == [[358, 359, 360]]
assert is_early_bird(400, 240) == [[610, 611, 612]]
assert is_early_bird(900, 888) == [[166, 167, 168], [2554, 2555, 2556], [2555, 2556, 2557], [2556, 2557, 2558], 'Early Bird!']
assert is_early_bird(1200, 745) == [[1263, 1264, 1265], [1613, 1614, 1615], [2125, 2126, 2127], 'Early Bird!']
assert is_early_bird(2000, 666) == [[122, 123, 124], [1888, 1889, 1890], [1889, 1890, 1891], [1890, 1891, 1892], [5555, 5556, 5557], 'Early Bird!']

print("Success")