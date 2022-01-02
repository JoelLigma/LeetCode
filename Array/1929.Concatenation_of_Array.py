# 1929. Concatenation of Array

# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
# Specifically, ans is the concatenation of two nums arrays.
# Return the array ans.

# Example 1:

# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]

class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return nums + nums
    
    
# space/time complexity analysis: O(n) as the input increases so does the time/space linearly
