"""
217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = dict()
        for i in range(len(nums)):
            if not nums[i] in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
            
            if d[nums[i]] > 1:
                return True
        return False
      
# time/space complexity: O(n)/O(n)
