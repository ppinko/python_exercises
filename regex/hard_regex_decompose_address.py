"""
https://edabit.com/challenge/7EFFraFvCYCfsdco8
"""

import re


def decompose_address(address: str) -> list:
    decomposed = []
    area = re.search(r'[A-Z]{2}', address)
    street_no = re.search(r'^\d+', address)
    area_no = re.search(r'\d+$', address)
    city = re.search(r'(?<=(St |Rd |Ct |Dr |Pl ))[^,]+', address)
    street_name = re.search(r'\w+\s(St|Rd|Ct|Dr|Pl)', address)
    for i in [street_no, street_name, city, area, area_no]:
        decomposed.append(str(i.group()))
    return decomposed


assert decompose_address("3315 Vanity St Beverly Hills, CA 90210") == ["3315", "Vanity St", "Beverly Hills", "CA", "90210"]
assert decompose_address("557 Farmer Rd Corner, MT 59105") == ["557", "Farmer Rd", "Corner", "MT", "59105"]
assert decompose_address("8919 Scarecrow Ct Idaho Falls, ID 80193") == ["8919", "Scarecrow Ct", "Idaho Falls", "ID", "80193"]
assert decompose_address("91 Ronald Dr Stenton, MS 39073") == ["91", "Ronald Dr", "Stenton", "MS", "39073"]
assert decompose_address("25000 Meek Pl Bozerman, MT 59104") == ["25000", "Meek Pl", "Bozerman", "MT", "59104"]

print('Success')