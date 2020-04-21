"""
https://edabit.com/challenge/knWLLoi87YbCmKJS4
"""


def happy(n):
    while True:
        temp = sum(pow(int(i), 2) for i in str(n))
        if temp == 1:
            return True
        elif temp == 4:
            return False
        n = temp
        
        
assert happy(100) == True
assert happy(101) == False
assert happy(102) == False
print('Success')