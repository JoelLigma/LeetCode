"""
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed_str = "".join(ch for ch in s if ch.isalnum()).lower()
        if processed_str == processed_str[::-1]:
            return True
        return False
# time complexity: O(s), where s is the size of the string
# space complexity: O(n), where n is the size of the processed string. We may also be able to reassign s to the processed string to save memory as it could make it O(1).

    def isPalindrome2(self, s: str) -> bool:
        res = ""
        for ch in s:
            ch = ch.lower()
            if ch.isalnum():
                res += ch
        
        # below can be replaced by res == res[::-1]
        reversed_res = ""
        for i in range(len(res) -1, -1, -1):
            reversed_res += res[i]
        return res == reversed_res

# Time complexity: O(n), where n is the size of the input str
# Space complexity: O(n), where n is the number of alpha numeric characters in the input str
