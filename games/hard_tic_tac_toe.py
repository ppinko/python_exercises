"""
https://edabit.com/challenge/TQfjTjj383kLhPnjE
"""


def who_won(board: list) -> str:
    cross_1 = [board[0][0], board[1][1], board[2][2]]
    cross_2 = [board[2][0], board[1][1], board[0][2]]
    if len(set(cross_1)) == 1:
        return cross_1[0]
    if len(set(cross_2)) == 1:
        return cross_1[0]
    for i in board:
        if len(set(i)) == 1:
            return i[0]
    k = list(zip(board))
    for i in k:
        if len(set(i[0])) == 1:
                return i[0][0]
    return 'Tie'


assert who_won([['X', 'O', 'B'],['B', 'X', 'O'],['B', 'B', 'X']]) == "X"
assert who_won([['X', 'O', 'X'],['O', 'X', 'B'],['X', 'B', 'O']]) == "X"
assert who_won([['X', 'X', 'O'],['O', 'O', 'X'],['X', 'X', 'O']]) == "Tie"
assert who_won([['X', 'X', 'B'],['O', 'X', 'X'],['O', 'O', 'O']]) == "O"

print('Success')