"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""


# Solution 1: Brute force

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx,elem in enumerate(nums):
            for idx2,elem2 in enumerate(nums):
                if idx != idx2:
                    if elem + elem2 == target:
                        return [idx,idx2]
                    
# Time/space complexity analysis: O(n**2) - beats 99.43% of Python submissions (runtime) & 99.99% of submissions (memory usage)


# Solution 2:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()

        for idx, value in enumerate(nums):
            difference = target - nums[idx]
            if difference in d:
                # as there is only one solution, we return it
                return [d[difference], idx] 
            d[value] = idx
        
"""
Explanation:

We keep track of the values and indices in the dictionary and find the two integers that add up to the target value.
E.g. target = 6 and value = 4
We subtract 4 from 6 == 2 and check if the exact value of the difference is already in the dictionary. If it is, we 
found the solution and can return the current index and the index of the value that is already in the dictionary by 
looking up the dictionary value (index) using the difference value as key.
if not, we continue to add the key, value pair (current value, index) to the dictionary and continue searching.

Time/space complexity analysis: O(n) - 127ms, beats 40.15% of Python submissions (runtime) & 61.63% of submissions (memory usage)


- adding value to dictionary O(1) 
- checking if a value exists in our hashmap/dictionary O(1) -> python dictionary uses hashing under the hood to find keys   so it's constant time
- we loop over the list only once
- the size of the dictionary may depend on the size of the input array as it is possible that we have to loop over the entire list to find the solution.
"""
