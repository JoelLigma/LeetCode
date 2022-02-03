"""
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
"""


# Solution 1: Brute Force + hashmap (should work theoretically but is really inefficient and even exceeds the time limit on LeetCode)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        
        """
        d = dict()
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if ((i != j) and (i != k) and (j != k)) and (nums[i] + nums[j] + nums[k] == 0):  
                        d[tuple(sorted([nums[i], nums[j], nums[k]]))] = 1
        return [list(l) for l in d.keys()]

# Time complexity: O(n**4)
# Space complexity: O(n**2)
      
  
# Solution 2: Two-Pointer (A little more efficient)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        
        """
        # we sort the array, fix one integer and then work with two pointers just like in the Two Sum problem
             
        # sort the array O(nlogn)
        nums = sorted(nums)
                
        # initialize hashmap to handle duplicate triplets
        d = dict()
        n = len(nums)
        
        # fix one integer
        for i in range(n - 2):
            # initialize the second and last index for each iteration
            l = i + 1
            r = n - 1
            while l < r:      
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum == 0: 
                    # keep track of the triplet as key, value arbitarily chosen as its not important
                    d[tuple(sorted([nums[i], nums[l], nums[r]]))] = 1
                    # now we can either increase the left pointer or decrease the right pointer
                    r -= 1 
                elif three_sum > 0:
                    r -= 1
                else:
                    l += 1
        return d
      
# Time complexity: O(n**2)  
# Space complexity: O(n) as we keep track of triplets using a dictionary which may scale with the number of triplets


# Alternative Solution without dictionary
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        
        """
        output = []
        n = len(nums)
        
        # sort the array O(nlogn)
        nums = sorted(nums)
                
        # fix one integer; ignore the last two
        for i in range(n - 2):
            
            # to handle duplicates for i, if duplicate found -> skip
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            # initialize the second and last index for each iteration
            l = i + 1
            r = n - 1
            
            while l < r:      
                if nums[i] + nums[l] + nums[r] == 0:
                    output += [[nums[i], nums[l], nums[r]]]
                    l += 1
                    # handling duplicates for l, if duplicate found -> skip by incrementing the left pointer
                    while l < r and nums[l] == nums[l-1]:
                        l += 1    
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
        return output
