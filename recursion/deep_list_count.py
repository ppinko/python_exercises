"""
https://edabit.com/challenge/nn7Na6zHLEHS9R8j2
"""

def deep_count(lst):
    count = 0
    for i in lst:
        count += 1
        if type(i) == list:
            count += deep_count(i)
    return count

print(deep_count([[1], [2], [3]]) == 6)
print(deep_count(["x", "y", ["z"]]) == 4)
print(deep_count(["a", "b", ["c", "d", ["e"]]]) == 7)
