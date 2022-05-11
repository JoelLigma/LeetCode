"""
448. Find All Numbers Disappeared in an Array

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
You may assume the returned list does not count as extra space.

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        countSort = [0] * (len(nums)+1)    
        for num in nums:
            countSort[num] += 1
            
        lst = []
        for i in range(1,len(nums)+1):
            if countSort[i] == 0:
                lst += [i]
        return lst
      
# time/space complexity: O(n)/O(1) as the prompt stated that the returned list does not count as extra space.
