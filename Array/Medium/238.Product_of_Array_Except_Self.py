"""
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 
Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""

# First shot at the problem (times out):
class Solution:
    def productExceptSelf(self, nums: list) -> int:

        l = 0
        r = len(nums) - 1

        res = [[] for i in range(len(nums))]
        temp_product = 1
        while l < len(nums):
            if l != r:
                temp_product *= nums[r]
                r -= 1
            elif r == l:
                r -= 1

            # reset for next value
            if r == -1:
                res[l] = temp_product
                temp_product = 1
                l += 1
                r = len(nums) - 1
        return res


# Better solution:
class Solution:
    def productExceptSelf(self, nums: list) -> int:
        n = len(nums)
        res = []

        forward_pass = [1 for i in range(len(nums) + 1)]
        backward_pass = [1 for i in range(len(nums) + 1)]
        
        temp = 1
        for i in range(1, len(forward_pass)):
            temp *= nums[i - 1]
            forward_pass[i] = temp
        
        temp = 1
        for i in range(len(backward_pass) - 1):
            temp *= nums[n - i - 1]
            backward_pass[n - i - 1] = temp

        for i in range(n):
            res += [forward_pass[i] * backward_pass[i + 1]]

        return res

# Time complexity: O(n), where n is the size of nums
# Space complexity: O(k), where k is the size of forward_pass
