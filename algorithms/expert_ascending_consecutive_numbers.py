"""
https://edabit.com/challenge/9iLhKgqZn5exBrmWm
"""


def ascending(n: str) -> bool:
    i = 1
    while i <= len(n) // 2:
        j, temp = 0, ''
        while j < len(n):
            a = n[j:j+i]
            temp += a
            if len(temp) == len(n):
                return True
            elif n[j+i:].find(str(int(a) + 1)) == 0:
                j += i
            else:
                break
        i += 1
    return False


assert ascending("232425") == True
assert ascending("444445") == True
assert ascending("1234567") == True
assert ascending("123412351236") == True
assert ascending("57585960616263") == True
assert ascending("500001500002500003") == True
assert ascending("919920921") == True

assert ascending("2324256") == False
assert ascending("1235") == False
assert ascending("121316") == False
assert ascending("12131213") == False
assert ascending("54321") == False
assert ascending("56555453") == False
assert ascending("90090190290") == False
assert ascending("35236237238") == False

print('Success')