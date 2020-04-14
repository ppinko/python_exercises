def sum_of_holes(n):
    tot = 0
    while n >= 1:
        temp = n
        while temp > 0:
            k = temp % 10
            if k in [0, 4, 6, 9]:
                tot += 1
            elif k == 8:
                tot += 2
            temp = temp // 10
        n -= 1
    return tot

assert sum_of_holes(1) == 0
assert sum_of_holes(4) == 1
assert sum_of_holes(6) == 2
assert sum_of_holes(8) == 4
assert sum_of_holes(9) == 5

print("Success")
