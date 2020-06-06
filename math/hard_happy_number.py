"""
https://edabit.com/challenge/4hFDo2uytDJmvKMfG
"""


def happy_algorithm(n: int) -> str:
    counter, nums, num = 0, [n], n
    while True:
        counter += 1
        temp = sum(pow(int(i), 2) for i in str(num))
        num = temp
        if temp == 1:
            return "HAPPY {0}".format(counter)
        elif temp in nums:
            return "SAD {0}".format(counter)
        else:
            nums.append(num)


assert happy_algorithm(139) == "HAPPY 5"
assert happy_algorithm(67) == "SAD 10"
assert happy_algorithm(1) == "HAPPY 1"
assert happy_algorithm(44) == "HAPPY 4"
assert happy_algorithm(89) == "SAD 8"
assert happy_algorithm(10) == "HAPPY 1"
assert happy_algorithm(1327) == "SAD 17"
assert happy_algorithm(2871) == "SAD 17"
assert happy_algorithm(3970) == "HAPPY 6"
assert happy_algorithm(5209) == "SAD 11"
assert happy_algorithm(6329) == "HAPPY 3"
assert happy_algorithm(8888) == "SAD 12"
assert happy_algorithm(9331) == "HAPPY 2"
assert happy_algorithm(10000) == "HAPPY 1"

print('Success')