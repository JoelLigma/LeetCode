"""
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_count, t_count = dict(), dict()
        for i in range(len(s)):
            if s[i] not in s_count:
                s_count[s[i]] = 1
            else:
                s_count[s[i]] += 1
            if t[i] not in t_count:
                t_count[t[i]] = 1
            else:
                t_count[t[i]] += 1
        
        for key in s_count:
            if key in s_count and key not in t_count:
                return False
            elif s_count[key] != t_count[key]:
                return False
        return True
# Time complexity: O(n+m) -> linear, where n is the size of s and m the size of t
# Space complexity: O(1), because there are only 26 characters in the English alphabet
