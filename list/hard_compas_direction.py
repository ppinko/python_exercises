"""
https://edabit.com/challenge/6LAgr6EGHKoZWGhjd
"""


def final_direction(direction, lst) -> str:
    directions = ('N', 'E', 'S', 'W')
    change = sum(1 if i == 'R' else -1 for i in lst)
    return directions[(directions.index(direction) + change) % 4]


assert final_direction('N', ['L', 'L', 'L']) == 'E'
assert final_direction('N', ['R', 'R', 'R', 'R', 'R', 'R', 'R']) == 'W'
assert final_direction('N', ['R', 'R', 'R', 'L']) == 'S'
assert final_direction('N', ['R', 'R', 'R', 'R']) == 'N'
assert final_direction('N', ['R', 'L']) == 'N'
assert final_direction('S', ['R', 'L', 'R', 'L', 'R']) == 'W'
assert final_direction('S', ['R', 'L', 'R', 'L', 'R', 'L']) == 'S'
assert final_direction('S', ['R', 'L', 'R', 'L', 'L', 'L']) == 'N'
assert final_direction('S', ['R', 'R']) == 'N'
assert final_direction('S', ['R']) == 'W'
assert final_direction('S', ['L']) == 'E'
assert final_direction('W', ['L', 'R', 'R']) == 'N'
assert final_direction('W', ['R', 'L', 'L']) == 'S'
assert final_direction('E', ['L', 'R', 'R']) == 'S'
assert final_direction('E', ['R', 'L', 'L']) == 'N'

print('Success')