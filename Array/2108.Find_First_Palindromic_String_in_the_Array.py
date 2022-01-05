# 2108. Find First Palindromic String in the Array

# Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".
# A string is palindromic if it reads the same forward and backward.

# Example 1:

# Input: words = ["abc","car","ada","racecar","cool"]
# Output: "ada"

# Solution:
# the key here is to know how to reverse a string

class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for word in words:
            if word == word[::-1]:
                return word
        return ""

# Space/time complexity analysis: O(n)
