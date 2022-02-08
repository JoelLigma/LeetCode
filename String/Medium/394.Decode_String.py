"""
394. Decode String

Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. 
For example, there will not be input like 3a or 2[4].

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
"""


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        
        for i in range(len(s)):
            if s[i] != "]":
                stack += [s[i]]
            else:
                temp_s = ""
                while stack[-1] != "[":
                    temp_s = stack.pop() + temp_s
                # pop the opening "["
                stack.pop()
                
                # next, get the multiplier number
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack += int(k) * temp_s
                
        return "".join(stack)
      
# Time complexity: O(s)    
