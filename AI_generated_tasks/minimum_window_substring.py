"""
Minimum Window Substring

Given two strings, s (the source string) and t (the target string), find the
smallest substring of s that contains all the characters in t, including
duplicates.

If no such substring exists, return an empty string "".

Example 1:
s = "ADOBECODEBANC"
t = "ABC"

✅ Output: "BANC"
🔍 Explanation: The smallest window in "ADOBECODEBANC" that contains 'A', 'B',
and 'C' is "BANC".

Example 2:
s = "AA"
t = "AA"

✅ Output: "AA"
🔍 Explanation: Since the entire string s is exactly t, it is the smallest
valid window.

Constraints:
✅ The input strings contain only uppercase and lowercase English letters.
✅ The length of s and t can be up to 10⁵.
✅ The answer must be found in O(n) time complexity.

Bonus Challenge:
⭐ Optimize space usage to O(k), where k is the number of unique characters in t.
⭐ Solve the problem using two-pointer/sliding window technique instead of brute
force.
"""


def min_window_substring(s: str, t: str) -> str:
    if not s or not t:
        return ""

    from collections import Counter, defaultdict

    dict_t = Counter(t)
    required = len(dict_t)

    l, r = 0, 0
    formed = 0
    window_counts = defaultdict(int)

    min_length = float("inf")
    min_left, min_right = 0, 0

    while r < len(s):
        char = s[r]
        window_counts[char] += 1

        if char in dict_t and window_counts[char] == dict_t[char]:
            formed += 1

        while l <= r and formed == required:
            char = s[l]

            if r - l + 1 < min_length:
                min_length = r - l + 1
                min_left, min_right = l, r

            window_counts[char] -= 1
            if char in dict_t and window_counts[char] < dict_t[char]:
                formed -= 1

            l += 1

        r += 1

    return "" if min_length == float("inf") else s[min_left : min_right + 1]


print(min_window_substring("ADOBECODEBANC", "ABC"))  # Output: "BANC"
print(min_window_substring("AA", "AA"))  # Output: "AA"
