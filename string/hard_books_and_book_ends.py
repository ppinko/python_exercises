"""
https://edabit.com/challenge/KMuRsbTKgZXoedMRN
"""


def count_unique_books(titles, bookend):
    s, flag = set(), False
    for i in titles:
        if flag and i != bookend:
            s.add(i)
        elif i == bookend and not flag:
            flag = True
        elif i == bookend and flag:
            flag = False
    return len(s)


assert count_unique_books("AZYWABBCATTTA", "A") == 4
assert count_unique_books("$AA$BBCATT$C$$B$", "$") == 3
assert count_unique_books("ZZABCDEF", "Z") == 0
assert count_unique_books("A#BBCD##GGA##!#", "#") == 6
assert count_unique_books("&AAAAAAAAAAAA&", "&") == 1
assert count_unique_books("&&&&&&&&", "&") == 0
assert count_unique_books("&A&&&&&&C&", "&") == 2
assert count_unique_books("&A&33333&C&", "&") == 2
assert count_unique_books("&3&3&3&", "&") == 1
assert count_unique_books("&4&3&3&", "&") == 2
assert count_unique_books("&AA&", "A") == 0
assert count_unique_books("AZAAABDZCCZZ", "Z") == 3
assert count_unique_books("AZAAABDZCCZZ", "A") == 1

print('Success')