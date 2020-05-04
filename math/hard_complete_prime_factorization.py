"""
https://edabit.com/challenge/XoBSfW4j6PNKerpBa
"""


def complete_factorization(num):
    ans = []
    for i in range(2, num+1):
        while num % i == 0:
            ans.append(i)
            num = num // i
        if num == 1:
            break
    return ans


assert complete_factorization(30) == [2, 3, 5]
assert complete_factorization(12) == [2, 2, 3]
assert complete_factorization(15) == [3, 5]
assert complete_factorization(48) == [2, 2, 2, 2, 3]
assert complete_factorization(311) == [311]
assert complete_factorization(17) == [17]
assert complete_factorization(44) == [2, 2, 11]
assert complete_factorization(10) == [2, 5]
assert complete_factorization(9) == [3, 3]
assert complete_factorization(72) == [2, 2, 2, 3, 3]

print('Success')