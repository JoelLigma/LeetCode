"""
136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]
Output: 1
"""

class Solution:
    # Solution 1: Set
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            if not num in s:
                s.add(num)
            else:
                s.remove(num)
        return list(s)[0]
    # time/space complexity: O(n)/O(n)
    
    # However, we are asked to solve this question with constant space so:
    
    # Solution 2: Bit manipulation XOR
    def singleNumber2(self, nums: List[int]) -> int:
        """
        All integers have a binary representation and we can use this to solve this problem.
        XOR - Intuition: if the bits are different the result is 1, else 0        
        - Zeroes in any XOR operation dont change the result.Thus, we can ignore these.
        - What's left over? The even number of 1's from the duplicate integers.
          Duplicates always cancel out and will therefore result in zero. 
        - Thus, the final result is 0 ^ the single number which will be our result.
        """
        out = 0
        for num in nums:
            out = out ^ num 
        return out
    # time/space complexity: O(n)/O(1)
