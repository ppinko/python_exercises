"""
Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""

def div_7_not_5(start, end):
    lsDiv7 = [str(i) for i in range(start, end + 1) if i%7 ==0 and i%5 != 0]
    ans = ", ".join(lsDiv7)
    return ans

a = 2000
b = 3200
print(div_7_not_5(a, b))