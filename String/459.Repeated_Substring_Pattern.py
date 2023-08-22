"""
459. Repeated Substring Pattern

Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        mid = (n // 2) + 1
        for i in range(1, mid):
            if s[:i] * (n // i) == s:
                return True
        return False

# Time complexity: O(n), where n is half the size of s
# Space complexity: O(1)


        
        
