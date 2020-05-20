"""
https://edabit.com/challenge/4afgmFpLP6CpwtRMY
"""


def sudoku_validator(lst: list) -> bool:
    k, box_score = len(lst), sum(range(1, 10))
    # checking rows
    if sum(0 if len(set(i)) != k or sum(i) != box_score else 1 for i in lst) != k:
        return False

    # checking columns
    transformed = list(zip(*lst))
    if sum(0 if len(set(i)) != k or sum(i) != box_score else 1 for i in transformed) != k:
        return False

    # checking boxes 3x3
    n = k // 3
    for i in range(n):
        for j in range(n):
            sub_L = []
            sub_L.extend(lst[3*i][3*j:3*(j+1)])
            sub_L.extend(lst[3 *i+1][3*j:3*(j + 1)])
            sub_L.extend(lst[3 *i+2][3 * j:3*(j + 1)])
            if sum(sub_L) != box_score:
                return False
    return True


assert sudoku_validator(
[ [ 1, 5, 2, 4, 8, 9, 3, 7, 6 ],
  [ 7, 3, 9, 2, 5, 6, 8, 4, 1 ],
  [ 4, 6, 5, 3, 7, 1, 2, 9, 8 ],
  [ 3, 8, 7, 1, 2, 4, 6, 5, 9 ],
  [ 8, 9, 1, 7, 6, 3, 4, 2, 5 ],
  [ 2, 4, 6, 5, 9, 8, 7, 1, 3 ],
  [ 9, 1, 4, 6, 3, 7, 5, 8, 2 ],
  [ 6, 2, 8, 9, 4, 5, 1, 3, 7 ],
  [ 5, 7, 3, 8, 1, 2, 9, 6, 4 ] ]) == False


assert sudoku_validator( [ [ 1, 5, 2, 4, 8, 9, 3, 7, 6 ],
  [ 7, 3, 9, 2, 5, 6, 8, 4, 1 ],
  [ 4, 6, 8, 3, 7, 1, 2, 9, 5 ],
  [ 3, 8, 7, 1, 2, 4, 6, 5, 9 ],
  [ 5, 9, 1, 7, 6, 3, 4, 2, 8 ],
  [ 2, 4, 6, 8, 9, 5, 7, 1, 3 ],
  [ 9, 1, 4, 6, 3, 7, 5, 8, 2 ],
  [ 6, 2, 5, 9, 4, 8, 1, 3, 7 ],
  [ 8, 7, 3, 5, 1, 2, 9, 6, 4 ] ]) == True


print('Success')