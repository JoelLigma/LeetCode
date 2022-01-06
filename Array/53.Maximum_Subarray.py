"""
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum. A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6


Solution: 

This problem can be solved using Kadane's algorithm. The algorithm runs on O(n) time and O(1) space. The following steps are necessary to implement the algorithm:

1. Initialize two variables e.g. current_sum and largest_sum to the first element of the array
2. Iterate over the elements in the array in range 1 to len(Array) in Python
3. Find the larger of max(current_sum + A[i], A[i]). We make use of the previous result to save space. 
4. If the current_sum + A[i] > largest_sum, we update the largest_sum variable with that value
5. Finally, we return the largest_sum
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest_sum = current_sum = nums[0]
        
        for i in nums[1:]:
            current_sum = max(current_sum + i, i)
            largest_sum = max(largest_sum, current_sum)
                
        return largest_sum
