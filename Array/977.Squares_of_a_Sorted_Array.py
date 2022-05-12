"""
977. Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
"""

#  Two-pointer
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = 0
        r = len(nums) - 1
        out_idx = len(nums) - 1
        out = [0] * len(nums)
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                out[out_idx] = nums[l]**2
                l += 1
            else:
                out[out_idx] = nums[r]**2
                r -= 1
            out_idx -= 1
        return out
        
# time/space complexity: O(n)/O(n)
