"""
https://edabit.com/challenge/TFG9f75apGi3SS49v
"""


def is_set(lst: list) -> bool:
    colors, numbers, shades, shapes = set(), set(), set(), set()
    for i in lst:
        colors.add(i['color'])
        numbers.add(i['number'])
        shades.add(i['shade'])
        shapes.add(i['shape'])
    sets = [colors, numbers, shades, shapes]
    return all(True if len(i) == 3 or len(i) == 1 else False for i in sets)


assert is_set( [{"color": "red", "number": 1, "shade": "lined", "shape": "squiggle"},
                {"color": "red", "number": 1, "shade": "lined", "shape": "diamond"},
                {"color": "red", "number": 1, "shade": "lined", "shape": "squiggle"}]) == False

assert is_set([{"color": "purple", "number": 3, "shade": "full", "shape": "oval"},
               {"color": "green", "number": 1, "shade": "full", "shape": "oval"},
               {"color": "red", "number": 3, "shade": "full", "shape": "oval"}]) == False

assert is_set([{"color": "red", "number": 1, "shade": "empty", "shape": "squiggle"},
               {"color": "red", "number": 2, "shade": "lined", "shape": "diamond"},
               {"color": "purple", "number": 3, "shade": "full", "shape": "oval"}]) == False

assert is_set([{"color": "red", "number": 1, "shade": "empty", "shape": "squiggle"},
               {"color": "red", "number": 1, "shade": "lined", "shape": "diamond"},
               {"color": "red", "number": 1, "shade": "lined", "shape": "oval"}]) == False

assert is_set([{"color": "red", "number": 1, "shade": "lined", "shape": "squiggle"},
               {"color": "red", "number": 1, "shade": "lined", "shape": "diamond"},
               {"color": "red", "number": 1, "shade": "lined", "shape": "oval"}]) == True

assert is_set([{"color": "red", "number": 1, "shade": "empty", "shape": "squiggle"},
               {"color": "red", "number": 2, "shade": "lined", "shape": "diamond"},
               {"color": "red", "number": 3, "shade": "full", "shape": "oval"}]) == True

assert is_set([{"color": "green", "number": 1, "shade": "empty", "shape": "squiggle"},
               {"color": "green", "number": 2, "shade": "empty", "shape": "diamond"},
               {"color": "green", "number": 3, "shade": "empty", "shape": "oval"}]) == True

assert is_set([{"color": "purple", "number": 1, "shade": "full", "shape": "oval"},
               {"color": "green", "number": 1, "shade": "full", "shape": "oval"},
               {"color": "red", "number": 1, "shade": "full", "shape": "oval"}]) == True

print('Success')