"""
https://edabit.com/challenge/E8TSTy4R5eWEkkaKf
"""


def is_valid(txt: str) -> bool:
    nums = txt.split('.')
    if len(nums) != 4:
        return False
    if not all(True if i.isdigit() else False for i in nums):
        return False
    if any(True if len(i) != 1 and i[0] =='0' else False for i in nums):
        return False
    digits = [int(i) for i in nums]
    if any(True if i > 255 or i < 0 else False for i in digits):
        return False
    return True


assert is_valid("1.2.3.4.5") == False
assert is_valid("123.45.67.89") == True
assert is_valid("123.456.78.90") == False 
assert is_valid("123.045.067.089") == False 
assert is_valid("") == False 
assert is_valid("abc.def.ghi.jkl") == False
assert is_valid("123.456.789.0") == False 
assert is_valid("12.34.56") == False 
assert is_valid("12.34.56 .1") == False
assert is_valid("12.34.56.-1") == False 
assert is_valid("123.045.067.089") == False
assert is_valid("192.168.1.1") == True 
assert is_valid("192.168.1.1  ") == False 
assert is_valid("  192.168.1.1") == False
assert is_valid("0.232.47.227") == True
assert is_valid("1e0.1e0.1e0.1e0") == False

print('Success')