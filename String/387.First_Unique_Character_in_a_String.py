"""
387. First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:

Input: s = "leetcode"
Output: 0
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = dict()
        for letter in s:
            if not letter in d:
                d[letter] = 1
            else:
                d[letter] += 1
        
        for key in d:
            if d[key] == 1:
                return s.index(key)
        return -1
      
# time complexity: O(n), where n is the size of the input string
# space complexity: O(1), because the dictionary will have at most 26 key-value pairs since the English alphabet contains 26 letters
