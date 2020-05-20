"""
https://edabit.com/challenge/eyJ4mN6RpyiRTvSob
"""


from collections import Counter


def is_palindrome_possible(txt: str) -> bool:
    counter = Counter(txt)
    return sum(1 for v in counter.values() if v % 2 == 1) <= 1


assert is_palindrome_possible("rearcac") ==  True
assert is_palindrome_possible("suhbeusheff") ==  True
assert is_palindrome_possible("palindrome") == False
assert is_palindrome_possible("yagnx") == False
assert is_palindrome_possible("zgzqxljjp") == False
assert is_palindrome_possible("tgmqkpdhnhatoco") == False
assert is_palindrome_possible("akyka") ==  True
assert is_palindrome_possible("kjyyrftnbsbq") == False
assert is_palindrome_possible("jynmynqhcy") == False
assert is_palindrome_possible("hfe") == False
assert is_palindrome_possible("noon") ==  True
assert is_palindrome_possible("azmkallbanpu") == False
assert is_palindrome_possible("drrede") ==  True
assert is_palindrome_possible("xmhwcocldjdnqvv") == False
assert is_palindrome_possible("reparpe") ==  True
assert is_palindrome_possible("jnavz") == False
assert is_palindrome_possible("orort") ==  True
assert is_palindrome_possible("mel") == False
assert is_palindrome_possible("jdxknf") == False
assert is_palindrome_possible("qo") == False
assert is_palindrome_possible("neett") ==  True
assert is_palindrome_possible("wow") ==  True
assert is_palindrome_possible("avkkiaapiusuapspiip") ==  True
assert is_palindrome_possible("aann") ==  True
assert is_palindrome_possible("iivcc") ==  True
assert is_palindrome_possible("akyka") ==  True
assert is_palindrome_possible("eelvl") ==  True
assert is_palindrome_possible("damam") == True 
assert is_palindrome_possible("mmo") == True 
assert is_palindrome_possible("ge") == False 
assert is_palindrome_possible("arrad") == True 
assert is_palindrome_possible("bq") == False 
assert is_palindrome_possible("djufyllynldw") == False 
assert is_palindrome_possible("reparpe") == True 
assert is_palindrome_possible("ttraoor") == True 
assert is_palindrome_possible("orort") == True 
assert is_palindrome_possible("asgas") == True 
assert is_palindrome_possible("t") == True 
assert is_palindrome_possible("tstsa") == True 
assert is_palindrome_possible("neett") == True 
assert is_palindrome_possible("wndnwrkpkihup") == False


print('Success')