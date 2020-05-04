"""
https://edabit.com/challenge/AJPB4jA3G5YxegGrk
"""


def decision(hand, face) -> str:
    colors, numbers = [], []
    for i in hand:
        l = i.split()
        colors.append(l[0])
        numbers.append(l[1])
    k = len(hand)
    if face.split()[0] in colors or face.split()[1] in numbers:
        k -= 1
    if k >= 2:
        return "Keep going..."
    elif k == 1:
        return "Uno!"
    else:
        return "You won!"


assert decision(['yellow 3', 'red 3'], 'red 10') == "Uno!"
assert decision(['blue 1'], 'blue 5') == "You won!"
assert decision(['red 1'], 'blue 5') == "Uno!"
assert decision(['red 1', 'blue 10'], 'blue 5') == "Uno!"
assert decision(['red 1', 'blue 10', 'green 7'], 'blue 5') == "Keep going..."
assert decision(['red 1', 'green 7'], 'green 2') == "Uno!"
assert decision(['green 7'], 'green 2') == "You won!"
assert decision(['blue 7'], 'green 7') == "You won!"
assert decision(['blue 1', 'green 2', 'yellow 4', 'red 2'], 'blue 5') == "Keep going..."

print('Success')