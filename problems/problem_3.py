# LINK: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Given a string s, find the length of the longest substring without repeating characters.


def length_of_longest_substring(s: str) -> int:
    if len(s) <= 1:
        return len(s)
    res = 0
    a, b = 0, 1
    while b <= len(s):
        if len(set(list(s[a:b]))) == len(s[a:b]):
            res = max(res, len(s[a:b]))
            b += 1
        else:
            a += 1
    return res
