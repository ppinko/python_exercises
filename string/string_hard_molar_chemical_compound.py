# https://edabit.com/challenge/M3qFgRyBpeTFjZbr3


def molar_mass(compound):
    chemicals = {'H':1, 'B':10, 'O':16, 'S':32, 'N':14, 'Cl':35}
    compounds = {'Water':"H2 O", 'BoricAcid':"H3 B O3", 'SulfuricAcid':"H2 S O4", 'NitricAcid':"H N O3", 'HydroChloricAcid':"H Cl"}

    name = compounds[compound]
    tot = 0
    for i in name.split():
        if i[-1].isdigit():
            tot += chemicals[i[:-1]] * int(i[-1])
        else:
            tot += chemicals[i]
    return tot


assert molar_mass("SulfuricAcid") == 98
assert molar_mass("Water") == 18
assert molar_mass("BoricAcid") == 61
assert molar_mass("NitricAcid") == 63
assert molar_mass("HydroChloricAcid") == 36

print("Success")