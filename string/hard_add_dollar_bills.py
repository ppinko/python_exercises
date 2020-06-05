"""
https://edabit.com/challenge/rBMsnM8HuGNSwkBCR
"""


def add_bill(bills: list) -> int:
    dollar_bills = [i[1:] for i in bills.split(',') if 'd' in i]
    dollar_bills_notes = [i[:-1] + '000' if 'k' in i else i for i in dollar_bills]
    return sum(int(i) for i in dollar_bills_notes)


assert add_bill("d200,p40,p60,d1k") ==1200
assert add_bill("d10,d40,p60,d200") ==250
assert add_bill("d10k,p500,p200") ==10000
assert add_bill("p400,d200,p40,p60") ==200
assert add_bill("d20k,d100,p40") ==20100
assert add_bill("p20k,p100,d100") ==100
assert add_bill("d100k") ==100000

print('Success')