"""
https://edabit.com/challenge/kusqKDBnX8g2uxRj8
"""


def correct_title(txt: str) -> str:
    excluded = {'of', 'and', 'the', 'in'}
    translated = []
    for i in txt.split():
        if '-' in i:
            temp = []
            for j in i.split('-'):
                if j.lower() not in excluded:
                    temp.append(j.capitalize())
                else:
                    temp.append(j.lower())
            translated.append('-'.join(temp))
        elif i.lower() not in excluded:
            translated.append(i.capitalize())
        else:
            translated.append(i.lower())
    return ' '.join(translated)


assert correct_title("sansa stark, lady of winterfell.") == "Sansa Stark, Lady of Winterfell."
assert correct_title("lord eddard stark, hand of the king.") == "Lord Eddard Stark, Hand of the King."
assert correct_title("jaime lannister, lord commander of the kingsguard.") == "Jaime Lannister, Lord Commander of the Kingsguard."
assert correct_title("varys, master of whisperers.") == "Varys, Master of Whisperers."
assert correct_title("doran martell, prince of dorne, lord of sunspear.") == "Doran Martell, Prince of Dorne, Lord of Sunspear."
assert correct_title("TYRION LANNISTER, HAND OF THE QUEEN.") == "Tyrion Lannister, Hand of the Queen."
assert correct_title("GRAND MAESTER PYCELLE.") == "Grand Maester Pycelle."
assert correct_title("EURON GREYJOY, KING OF THE IRON ISLANDS, LORD REAPER OF PYKE.") == "Euron Greyjoy, King of the Iron Islands, Lord Reaper of Pyke."
assert correct_title("PETYR BAELISH, LORD PROTECTOR OF THE VALE.") == "Petyr Baelish, Lord Protector of the Vale."
assert correct_title("MANCE RAYDER, KING-BEYOND-THE-WALL.") == "Mance Rayder, King-Beyond-the-Wall."
assert correct_title("jOn SnoW, kINg IN thE noRth.") == "Jon Snow, King in the North."
assert correct_title("Jeor MORMONT, Lord COMMANDER of the NIGHT'S WATCH.") == "Jeor Mormont, Lord Commander of the Night's Watch."
assert correct_title("cERSei LANnIStEr, QuEEn Of the aNdals and THE fIRSt men, PROtecTOR OF tHe SEVEN KInGdOmS.") == "Cersei Lannister, Queen of the Andals and the First Men, Protector of the Seven Kingdoms."
assert correct_title("DAeneRYS StOrmboRn oF hOuse TARGARYEn, ThE FirsT OF HER naMe, QUeEn OF The ANdAlS And THe FirsT mEN, PROtECtOr Of tHE SEven KinGDOmS, The MoTHeR of DrAGONS, thE KhALeEsi oF THE GReAt gRAss sEa, The UnburNT, The BReakEr of cHAInS.") == "Daenerys Stormborn of House Targaryen, the First of Her Name, Queen of the Andals and the First Men, Protector of the Seven Kingdoms, the Mother of Dragons, the Khaleesi of the Great Grass Sea, the Unburnt, the Breaker of Chains."

print('Success')