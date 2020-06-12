"""
https://edabit.com/challenge/PirFJDfGk4vpsdkeE
"""


def help_bobby(size):
    array = [[0 for i in range(size)] for _ in range(size)]
    row = 0
    for column in range(size):
        array[column][row] = 1
        array[size-column-1][row] = 1
        row += 1
    return array


assert help_bobby(1) == [[1]]
assert help_bobby(2) == [[1, 1], [1, 1]]
assert help_bobby(5) == [[1, 0, 0, 0, 1], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]]
assert help_bobby(8) == [[1, 0, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0, 0, 1]]

print('Success')