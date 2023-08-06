""""
7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 
Constraints:
-231 <= x <= 231 - 1
"""

class Solution:
    def reverse(self, x: int) -> int:
        isNeg = x < 0
        if isNeg:
            x *= -1

        revX = 0
        while x > 0:
            revX = revX * 10 + x % 10
            x = x // 10
            if revX > 2**31 or revX < -2**31:
                return 0
         
        if isNeg:
            revX *= -1
        return revX       
    
# Time complexity: O(N), where N is the size of the integer's number of digits
# Space complexity: O(1), since we only initialise a counter to store the reversed integer
