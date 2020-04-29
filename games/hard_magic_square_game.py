"""
https://edabit.com/challsenge/shf4iTJTbQ7sethFA
"""


def magic_square_game(A, B):
    return A[1][B[0] - 1] == B[1][A[0] - 1]


assert magic_square_game([2,'100'],[1,'101']) == False
assert magic_square_game([2,'001'],[1,'101']) == True
assert magic_square_game([3,'111'],[2,'011']) == True
assert magic_square_game([1,'010'],[3,'101']) == False
assert magic_square_game([2,'111'],[3,'011']) == True
assert magic_square_game([2,'100'],[3,'110']) == False
assert magic_square_game([1,'001'],[1,'101']) == False
assert magic_square_game([2,'100'],[2,'101']) == True
assert magic_square_game([3,'010'],[1,'110']) == True
assert magic_square_game([1,'100'],[2,'110']) == False
assert magic_square_game([2,'111'],[3,'011']) == True
assert magic_square_game([2,'001'],[2,'101']) == True
assert magic_square_game([1,'100'],[2,'101']) == False
assert magic_square_game([3,'001'],[3,'011']) == True
assert magic_square_game([3,'111'],[1,'110']) == False
assert magic_square_game([2,'100'],[2,'101']) == True

print('Success')