"""
https://edabit.com/challenge/i35wfM7KEdpnK45mD
"""

def makePlusFunction(base_num: int):
    def add_next(num: int) -> int:
        return base_num + num
    return add_next

plusTwo = makePlusFunction(2)
plusFive = makePlusFunction(5)
plusSeven = makePlusFunction(plusTwo(plusFive(0)))
plusTen = makePlusFunction(10)

assert plusTwo(0) == 2
assert plusTwo(18) == 20
assert plusTwo(-1) == 1
assert plusFive(0) == 5
assert plusFive(12) == 17
assert plusFive(-5) == 0
assert plusSeven(0) == 7
assert plusSeven(41) == 48
assert plusSeven(-117) == -110
assert plusTen(0) == 10
assert plusTen(1) == 11
assert plusTen(-1) == 9
assert plusTwo(plusFive(plusSeven(plusTen(1)))) == 25

assert makePlusFunction(8)(8) == 16
assert makePlusFunction(-100)(0) == -100
assert makePlusFunction(1)(100) == 101
assert makePlusFunction(0)(0) == 0

print("Success")
