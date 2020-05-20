"""
https://edabit.com/challenge/NtsqbRPqtPYhR8tJe
"""


def blocks(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 5
    tot, step = 5, 7
    for i in range(1, n):
        tot += step
        step += 1
    return tot


""" Alternative solution """


def blocks(step):
	return 5*step + sum(range(2,step+1))


assert blocks(77) == 3387
assert blocks(33) == 725
assert blocks(50) == 1524

print("Success")