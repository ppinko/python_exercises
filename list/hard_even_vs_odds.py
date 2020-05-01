"""
https://edabit.com/challenge/4gDNqQB355FFGFFWN
"""


def available_spots(lst: list, num: int) -> int:
    if num % 2 == 0:
        x = 'even'
    else:
        x = 'odd'
    total = 0
    if x == 'even':
        for i in range(len(lst) - 1):
            if lst[i] % 2 == 0 or lst[i+1] % 2 == 0:
                total += 1
    else:
        for i in range(len(lst) - 1):
            if lst[i] % 2 == 1 or lst[i+1] % 2 == 1:
                total += 1
    return total


assert available_spots([0, 4, 6, 8], 9) == 0
assert available_spots([0, 4, 6, 8], 6) == 3
assert available_spots([1, 2, 3, 4], 6) == 3
assert available_spots([1, 2, 3, 4], 5) == 3
assert available_spots([1, 1, 1, 4], 7) == 3
assert available_spots([1, 1, 4, 4], 7) == 2
assert available_spots([1, 4, 4, 4], 7) == 1
assert available_spots([4, 4, 4, 4], 7) == 0
assert available_spots([5, 5, 5, 8, 8, 5, 5, 5, 5], 32) == 3
assert available_spots([4, 4], 8) == 1

print('Success')