"""
https://edabit.com/challenge/mfKmMv28DicrAhrkJ
"""


def hex_color_mixer(lst: list) -> str:
    R, G, B = [], [], []
    for i in lst:
        R.append(int(str(i[1:3]), 16))
        G.append(int(str(i[3:5]), 16))
        B.append(int(str(i[5:7]), 16))
    colors = [R, G, B]
    mixed_color = '#'
    for i in colors:
        temp = str(hex(int(round(0.0000001 + sum(i) / len(i), 0))))[2:].upper()
        if len(temp) == 1:
            temp += '0'
        mixed_color += temp
    return mixed_color


assert hex_color_mixer(["#FFFF00", "#FF0000"]) == "#FF8000"
assert hex_color_mixer(["#FFFF00", "#0000FF"]) == "#808080"
assert hex_color_mixer(["#B60E73", "#0EAEB6"]) == "#625E95"
assert hex_color_mixer(["#FF0000", "#00FF00", "#0000FF"]) == "#555555"
assert hex_color_mixer(["#99CC00", "#663399", "#1A8191"]) == "#5E8063"
assert hex_color_mixer(["#918381", "#D53B21", "#A54C83", "#DEFACF"]) == "#BA817D"
assert hex_color_mixer(["#140A23", "#46B31E", "#CFDF08", "#263534", "#EAD1FB", "#235E02"]) == "#65803F"
assert hex_color_mixer(["#FFFFFF", "#000000", "#000000", "#FFFFFF"]) == "#808080"
assert hex_color_mixer(["#CCCCCC"]) == "#CCCCCC"

print('Success')