"""
https://edabit.com/challenge/YifX9gJwnu5MS9brs
"""


def samples_from_curve(points, shape):
    if shape == 'linear':
        return [0] + [ i / (points - 1) for i in range(1, points)]
    elif shape == 'pow':
        return [0] + [round(pow(i / (points - 1), 2), 2) for i in range(1, points)]
    else:
        return [0] + [round(pow(i / (points - 1), 0.5), 2) for i in range(1, points)]


# Linear
assert samples_from_curve(2, 'linear') == [0, 1]
assert samples_from_curve(3, 'linear') == [0, 0.5, 1]
assert samples_from_curve(11, 'linear') == [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

# Pow
assert samples_from_curve(4, 'pow') == [0, 0.11, 0.44, 1]
assert samples_from_curve(5, 'pow') == [0, 0.06, 0.25, 0.56, 1]
assert samples_from_curve(11, 'pow') == [0, 0.01, 0.04, 0.09, 0.16, 0.25, 0.36, 0.49, 0.64, 0.81, 1]

# Sqrt
assert samples_from_curve(6, 'sqrt') == [0, 0.45, 0.63, 0.77, 0.89, 1]
assert samples_from_curve(7, 'sqrt') == [0, 0.41, 0.58, 0.71, 0.82, 0.91, 1]
assert samples_from_curve(11, 'sqrt') == [0, 0.32, 0.45, 0.55, 0.63, 0.71, 0.77, 0.84, 0.89, 0.95, 1]

print('Success')