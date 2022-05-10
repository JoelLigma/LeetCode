"""
414. Third Maximum Number

Given an integer array nums, return the third distinct maximum number in this array. 
If the third maximum does not exist, return the maximum number.

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
"""

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # this solution works but it not exactly scalable for nth max number.
        first_max = float("-inf")
        second_max = float("-inf")
        third_max = float("-inf")
        
        for num in nums:

            if num > first_max:
                # since we have a new first_max the old first_max becomes the second_max etc.
                third_max = second_max
                second_max = first_max
                first_max = num
            elif num > second_max and num < first_max:
                # since we have a new second_max the old second_max becomes the third_max
                third_max = second_max
                second_max = num
            elif num > third_max and num < second_max:
                third_max = num
        
        if third_max == float("-inf") or second_max == float("-inf"):
            return first_max
        return third_max
        
 # Time/space complexity: O(n)/O(1)
