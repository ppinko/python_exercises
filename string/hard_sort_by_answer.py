"""
https://edabit.com/challenge/9zf6scCreprSaQAPq
"""


def sort_by_answer(lst: list) -> list:
    lst = [i.replace('x', '*') for i in lst]    # replace 'x' with '*'
    answers = [eval(i) for i in lst]            # calculate and store expressions
    temp = [i[0] for i in sorted(zip(lst, answers), key=lambda x:x[1])] # sort by value
    return [i.replace('*', 'x') for i in temp]  # replace '*' with '#' backwards


assert sort_by_answer(["1 + 1", "1 + 7", "1 + 5", "1 + 4"]) == ["1 + 1", "1 + 4", "1 + 5", "1 + 7"]
assert sort_by_answer(["2 + 2", "2 - 2", "2 x 2", "2 / 2"]) == ["2 - 2", "2 / 2", "2 + 2", "2 x 2"]
assert sort_by_answer(["1 x 1", "3 x 3", "-1 x -1", "-3 x -3"]) == ["1 x 1", "-1 x -1", "3 x 3", "-3 x -3"]
print('Success')