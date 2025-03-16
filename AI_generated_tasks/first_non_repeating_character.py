'''
Challenge: First Non-Repeating Character
Given a string, find the first non-repeating character and return its index. 
If all characters repeat, return -1.

Example Input 1:
s = "leetcode"

Expected Output:
0  # 'l' is the first non-repeating character

Example Input 2:
s = "aabb"

Expected Output:
-1  # All characters repeat

Constraints:
- Solve in O(n) time complexity.
- Consider both lowercase and uppercase letters.
- Assume 's' contains only English letters (a-z, A-Z).
'''

def first_non_repeating_character(s: str) -> int:
    n = -1
    lower_cases = s.lower()
    chars_dict = dict()
    for i, char in enumerate(lower_cases):
        if char.lower() in chars_dict.keys():
            chars_dict[char].append(i)
        else:
            chars_dict[char] = [i]
    singular_chars = [v[0] for v in chars_dict.values() if len(v) == 1]
    return  singular_chars[0] if len(singular_chars) > 0 else n

s1 = "leetcode"
s2 = "aabb"
s3 = "aNanas"

print(first_non_repeating_character(s1))
print(first_non_repeating_character(s2))
print(first_non_repeating_character(s3))