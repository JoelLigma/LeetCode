# 1920. Build Array from Permutation

# Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.
# A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

# Example 1:

# Input: nums = [0,2,1,5,3,4]
# Output: [0,1,2,4,5,3]


# Solution 1: For Loop

class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        
        for i in range(len(nums)):
            output += [nums[nums[i]]]
            
        return output
    
# time/space complexity analysis: O(n)



# Solution 2: List Comprehension

class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
            
        return [nums[i] for i in nums]    
        
# time/space complexity analysis: O(n)

