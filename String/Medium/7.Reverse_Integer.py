"""
7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], 
then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
"""

class Solution:
    def reverse(self, x: int) -> int:

        if x >= 0:  
            str_int = str(x)
            out = int(str_int[::-1])
        else:
            x *= -1
            str_int = str(x)
            out = int(str_int[::-1]) * -1

        if out < -2**31 or out > 2**31-1:
            return 0
        return out
      
 # time/space complexity: O(n), where n is the size of the integer converted to str. Space: O(1)
