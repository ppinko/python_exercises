'''
Challenge: Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating 
characters.

Example Input 1:
s = "abcabcbb"

Expected Output:
3  # "abc" is the longest unique substring

Example Input 2:
s = "bbbbb"

Expected Output:
1  # "b" is the longest unique substring

Example Input 3:
s = "pwwkew"

Expected Output:
3  # "wke" is the longest unique substring

Constraints:
* Solve it in O(n) time complexity.
* Can you solve it using the sliding window technique?
'''

def longest_substring_without_repeating_characters(s: str) -> int:
    n = 0
    i, j = 0, 1 # indexes to evaulate substring of the string
    while j <= len(s):
        # if length of substring equals lengs of set from substring, it means 
        # that all chars are unique
        if len(s[i:j]) == len(set(s[i:j])):
            if len(s[i:j]) > n:
                n = len(s[i:j])
            j += 1
        # if there is mismatch in length of substring and set, cut char from left
        elif i+1 != j:
            i += 1
    return n
    
s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"

print(longest_substring_without_repeating_characters(s1))
print(longest_substring_without_repeating_characters(s2))
print(longest_substring_without_repeating_characters(s3))


def longest_unique_substring(s):
    seen = set()
    left = max_length = 0

    for right in range(len(s)):
        while s[right] in seen:  # Remove characters from the left until unique
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length

print(longest_unique_substring(s1))
print(longest_unique_substring(s2))
print(longest_unique_substring(s3))