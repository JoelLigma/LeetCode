"""
9. Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-2**31 <= x <= 2**31 - 1
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        out = str(x)
        return out == out[::-1]
    
    def isPalindrome2(self, x: int) -> bool:
        out = str(x)
        reversedX = ""

        for i in range(len(out) - 1, -1, -1):
            reversedX += out[i]

        return out == reversedX

    def isPalindrome3(self, x: int) -> bool:
        """
        Intuition: There is a way to check if an integer is a palindrome by only reversing the latter 
        half of it and checking whether it equals the first half of the original integer.

        Example, if x = 15951, then let's create reverse of x in loop. Initially, x = 15951, revX = 0

        x = 1595, revX = 1
        x = 159, revX = 15
        x = 15, revX = 159

        After the third iteration revV > x thus we crossed the halfway point of the odd integer.
        For even length integers we would stop directly in the middle

        Now to check if the integer is a palindrome we can 
        - check if x == revX for even length integer
        - check if x == revX // 10 for odd length integer
        """
        if x < 0 or (x % 10 == 0 and x > 0):
            return False

        revX = 0
        while x > revX:
            revX = revX * 10 + x % 10
            x = x // 10        
        return x == revX or x == revX // 10

# Time complexity: O(N), where n is the size of x
# Space complexity: O(N), where n is the size of x
