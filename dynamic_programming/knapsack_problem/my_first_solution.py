"""
https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
"""


def knapsack(values, weights, capacity, total):
    if len(values) == 0 or capacity - weights[0] < 0:
        return total
    else:
        return max(knapsack(values[1:], weights[1:], capacity - weights[0], total + values[0]),
                   knapsack(values[1:], weights[1:], capacity, total))


assert knapsack([60, 100, 120], [10, 20, 30], 50, 0) == 220
assert knapsack([135, 139, 149, 150, 156, 163, 173, 184, 192, 201, 210, 214, 221, 229, 240],
                [70, 73, 77, 80, 82, 87, 90, 94, 98, 106, 110, 113, 115, 118, 120],
                750, 0) == 1458
print('Success')
