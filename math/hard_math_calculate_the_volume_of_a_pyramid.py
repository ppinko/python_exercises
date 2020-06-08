"""
https://edabit.com/challenge/crpyJZJq2k78tiHNd
"""


def pyramid_volume(l, w, h, unit):
    value = l * w * h / 3
    convert = {"meters": 1, "centimeters": 1000000, "millimeters": 1000000000,
               "kilometers": 0.000000001}
    return "{0:.3f} cubic {1}".format(round(value * convert[unit], 3), unit)


assert pyramid_volume(10, 14, 6, "meters") == "280.000 cubic meters"
assert pyramid_volume(8, 12, 2, "centimeters") == "64000000.000 cubic centimeters"
assert pyramid_volume(92, 1245, 1923, "kilometers") == "0.073 cubic kilometers"
assert pyramid_volume(19, 254, 21, "millimeters") == "33782000000000.000 cubic millimeters"
assert pyramid_volume(13.6, 62.2, 6, "meters") == "1691.840 cubic meters"
assert pyramid_volume(4230, 923, 1932, "kilometers") == "2.514 cubic kilometers"

print("Success")