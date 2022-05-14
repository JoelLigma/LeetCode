"""
189. Rotate Array (medium)

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums) # <- this is the key to this solution as this allows us to keep track of the rotation if k exceeds the number of elements in nums
        l, r = 0, len(nums)-1
        
        def reverse(l,r,nums):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            return nums
          
        nums = reverse(l=l, r=r, nums=nums)
        # print(nums)
        nums = reverse(l=l, r=k-1, nums=nums)
        # print(nums)
        nums = reverse(l=k, r=len(nums)-1, nums=nums)
        # print(nums)
        
  # time/space complexity: O(n)/O(1)
