"""
905. Sort Array By Parity

Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
Return any array that satisfies this condition.


Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
"""

# The solution is very similar to the "Move Zeroes" problem where we use a swap operation.
class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = 0
        for r in range(len(nums)):
            if nums[r] % 2 == 0:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
        return nums
      
# time/space complexity: O(n)/O(1) 
