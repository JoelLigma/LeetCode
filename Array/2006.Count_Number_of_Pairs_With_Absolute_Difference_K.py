"""
2006. Count Number of Pairs With Absolute Difference K

Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.
The value of |x| is defined as:

x if x >= 0.
-x if x < 0.
 
Example 1:

Input: nums = [1,2,2,1], k = 1
Output: 4
"""


# Solution 1:
class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    count += 1   
        return count
      
# Time complexity: O(n**2)
# Space complexity: O(1)
