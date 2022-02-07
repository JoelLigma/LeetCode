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


# Solution 1: Brute Force
class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counter = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    counter += 1   
        return counter
      
# Time complexity: O(n^2)
# Space complexity: O(1)


# Solution 2: Hashmap
class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """ 
        import collections
        """
        Defaultdict() is part of the collections module. Defaultdict means that if a key is not found in the dictionary,
        then instead of a KeyError being thrown a new entry is created. The type of this new entry is given by the
        argument of defaultdict, e.g. defaultdict(int).
        """
        d = defaultdict(int)
        c = 0
        for num in nums:
            c += d[num-k] + d[num+k]
            d[num] += 1
        return c
   
# Time complexity: O(n)
# Space complexity: O(n)
