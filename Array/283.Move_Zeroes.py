"""
283. Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""

class Solution(object):
    # Solution 1: First attempt. While it does the job it is obviously not efficient and we dont want that.
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        c = 0
        while i < len(nums)-1-c:            
            if nums[i] == 0:
                c += 1
                for j in range(i, len(nums)-1):
                    nums[j] = nums[j+1]
                nums[-1] = 0
            else:
                i += 1
    # time/space complexity: O(n**2)/O(1)

    
    # Solution 2: a more optimal solution using a swap operation that occurs in other algorithms (e.g. quicksort) as well.
    def moveZeroes2(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
    # time/space complexity: O(n)/O(1)
