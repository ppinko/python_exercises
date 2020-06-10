"""
https://edabit.com/challenge/iLLqX4nC2HT2xxg3F
"""


def deepest(L: list) -> int:
    counter, ans = 0, 0
    for char in str(L):
        if char == '[':
            counter += 1
            if counter > ans:
                ans = counter
        elif char == ']':
            counter -= 1
    return ans


""" Alternative recursive solution """
def deepest(lst):
	if type(lst)!= list: return 0
	return 1 + max(deepest(e) for e in lst)


assert deepest([1, 4, 5]) == 1
assert deepest([[2, 3], 4, [6, 7, [8]]]) == 3
assert deepest([5, [[[[[[[[[[2]]]]]]]]]], [[[[[[[[[[[[4]]]]]]]]]]]]]) == 13
assert deepest([[[3, 2, [[4]], 8], [[2, 4], 5]], 3, 5, [9, 1]]) == 5
assert deepest([[6, 9, 6], [[[1, 4], 0, 8], [8, 0, [4, 1]]], [[5, 3, 4], [4, 3, 5]]]) == 4

print("Success")