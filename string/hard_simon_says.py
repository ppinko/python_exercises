"""
https://edabit.com/challenge/soYjr9KM2YkGurtiT
"""

def simon_says(lst: list) -> int:
    x = 0
    for i in lst:
        row = i.split()
        if row[0] != 'Simon':
            continue
        if row[-2] == 'add':
            x += int(row[-1])
        elif row[-2] == "subtract":
            x -= int(row[-1])
        elif row[-2] == "by":
            x *= int(row[-1])
    return x


assert simon_says(["Simon says multiply by 33", "Sarah says subtract 19", "Now subtract 32", "Next, add 41", "Simeon says subtract 27", "Firstly, multiply by 48", "Then multiply by 46", "Simon says subtract 41", "Now multiply by 50", "Simon says subtract 6", "Simon says add 20", "Sieon says add 47", "Sarah says subtract 13", "Next, add 49", "Simon says multiply by 2", "Simon says subtract 50", "Simon says subtract 47", "Now subtract 7", "Joshua says subtract 21", "Simon says multiply by 3"]) == -453
assert simon_says(["Simon says add 14", "Simon says add 24"]) == 38
assert simon_says(["Simon says subtract 34", "John says add 1", "Simon says subtract 40", "Next, multiply by 7", "Firstly, subtract 10", "Next, add 13", "Simon says multiply by 36", "Now multiply by 7", "Now multiply by 6", "Next, multiply by 19", "Simon says multiply by 47", "Simeon says multiply by 40", "Simon says subtract 13", "Joshua says multiply by 45", "Simeon says multiply by 1", "Simon says add 32", "Next, multiply by 28"]) == -125189
assert simon_says(["Then multiply by 6"]) == 0
assert simon_says(["Simon says multiply by 48", "Firstly, subtract 14", "Next, add 46", "John says add 44", "Simon says multiply by 16", "Firstly, subtract 42", "Firstly, add 34", "Then multiply by 26", "Then multiply by 32", "Simeon says add 40", "Simon says multiply by 48", "Sarah says multiply by 46"]) == 0
assert simon_says(["Next, multiply by 20", "Sarah says subtract 18", "Now add 47", "Sarah says multiply by 4", "Simon says subtract 47", "Simon says multiply by 31", "Firstly, multiply by 39"]) == -1457
assert simon_says(["Firstly, multiply by 13"]) == 0
assert simon_says(["Sieon says add 29", "Next, multiply by 14", "Sieon says multiply by 25", "Simon says subtract 10", "Simeon says add 39", "Simeon says multiply by 13", "Simon says multiply by 8", "Next, subtract 18", "Next, add 28", "Simon says add 11", "Next, add 5", "John says add 21"]) == -69
assert simon_says(["Sarah says multiply by 35", "Then multiply by 11", "Simeon says subtract 5"]) == 0
assert simon_says(["Firstly, multiply by 4", "Now multiply by 4", "Firstly, add 40", "John says add 30", "Simon says multiply by 35"]) == 0
assert simon_says(["Next, subtract 27", "Next, subtract 33", "Then multiply by 3", "Simon says add 46", "Next, subtract 48", "Now add 37", "Simon says subtract 29", "Next, add 14"]) == 17
assert simon_says(["Simon says subtract 48", "John says subtract 50", "Sieon says subtract 6", "Simon says subtract 4", "Sieon says subtract 10", "Now multiply by 46", "Now multiply by 44", "Simeon says multiply by 23", "Simon says multiply by 18", "Now subtract 8", "Then subtract 49", "Simon says subtract 48", "Simon says add 43"]) == -941
assert simon_says(["Then multiply by 26", "Simon says add 37", "Now subtract 28", "Now add 3", "Next, add 5", "Simeon says multiply by 42", "Simon says subtract 45", "Firstly, multiply by 30", "Now add 11"]) == -8
assert simon_says(["Simon says add 6", "Sieon says multiply by 3", "Then add 48", "Next, subtract 48", "Simon says multiply by 9", "Simon says add 10", "Simeon says multiply by 41", "Simon says subtract 8", "Next, add 1", "Then add 31", "Simon says subtract 37", "Simon says multiply by 3", "Now multiply by 10", "Then add 33", "Firstly, multiply by 17", "Next, multiply by 20", "Simeon says multiply by 28", "Sieon says multiply by 28", "Then add 32", "Then add 34"]) == 57
assert simon_says(["Simeon says subtract 27", "Next, add 31", "Firstly, subtract 16", "Sieon says add 5", "Firstly, multiply by 49", "Firstly, add 20", "Now multiply by 11", "Simon says add 43", "Simon says add 48", "Simeon says multiply by 9", "Sieon says subtract 50", "Now multiply by 14", "Firstly, subtract 14", "Then multiply by 27", "Sieon says multiply by 23", "Simon says subtract 33", "Simon says multiply by 45", "Firstly, subtract 25"]) == 2610

print('Success')