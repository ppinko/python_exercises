"""
https://edabit.com/challenge/LEFxqpwii5DRLMZRJ
"""


def make_number(n: int) -> list:
    ans = []
    for i in range(1, n // 2 + 1):
        temp, consecutive, j = [], i, i
        temp.append(i)
        while consecutive < n:
            j += 1
            consecutive += j
            temp.append(j)
            if consecutive == n:
                ans.append(temp)
    return ans


assert make_number(9) == [[2,3,4], [4,5]]
assert make_number(8) == []
assert make_number(100) == [[9,10,11,12,13,14,15,16], [18,19,20,21,22]]
assert make_number(5) == [[2,3]]
assert make_number(18) == [[3,4,5,6], [5,6,7]]
assert make_number(40) == [[6,7,8,9,10]]
assert make_number(1) == []
assert make_number(3) == [[1, 2]]

print('Success')