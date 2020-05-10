"""
https://edabit.com/challenge/HZZp3NCaZ5r67zboj

Musical instruments have a range of notes to play, some instruments having a much larger range than others.

Given the following ranges for the instrument, create a function that returns True if a given note is within
a given instrument's range. Otherwise, return False.

Instrument	Range
Piccolo	D4-C7
Tuba	D1-F4
Guitar	E3-E6
Piano	A0-C8
Violin	G3-A7
"""


def instrument_range(instrument, sound) -> bool:
    d = {'Piccolo': ('D4', 'C7'), 'Tuba':('D1', 'F4'), 'Guitar': ('E3', 'E6'),
          'Piano': ('A0', 'C8'), 'Violin': ('G3', 'A7')}
    s_range = d[instrument]
    if s_range[0][0] < sound[0] < s_range[1][0]:
        return True
    elif s_range[0][1] < sound[1] < s_range[1][1]:
        return True
    elif sound[0] == s_range[0][0]:
        if sound[0] < s_range[1][0] or sound[1] <= s_range[1][1]:
            return True
        else:
            return False
    elif sound[0] == s_range[1][0]:
        if sound[1] <= s_range[1][1]:
            return True
        else:
            return False
    elif sound[1] == s_range[0][1]:
        if sound[1] < s_range[1][1]:
            return True
        else:
            return False
    else:
        return False


assert instrument_range("Piccolo", "A3") == False
assert instrument_range("Violin", "G6") == True
assert instrument_range("Piano", "C8") == True
assert instrument_range("Piano", "C9") == False
assert instrument_range("Tuba", "C8") == False
assert instrument_range("Guitar", "F4") == True
assert instrument_range("Guitar", "C4") == True
assert instrument_range("Piccolo", "F4") == True
assert instrument_range("Tuba", "F6") == False

print('Success')