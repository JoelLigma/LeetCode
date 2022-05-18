"""
28. Implement strStr()

Implement strStr().
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
"""

class Solution:
    # Solution 1: For loop
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) + 1 - len(needle)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
    # Time complexity: O(n), where n is the haystack string
    # Space complexity: O(1)
    # However, it may be possible that the questions asks for the application of the Knuth-Morris-Pratt (KMP) algorithm or Rabin-Karp string matching algorithm.
