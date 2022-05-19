"""
704. Binary Search

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
"""

class Solution:
    # Solution 1: Iterative solution (preferred) 
    def search(self, nums: List[int], target: int) -> int:
        """
        Integers are sorted in ascending order.
        Integers are unique.
        Target may or may not exist.
        
        Solution: Binary search
        """        
        # initialise the pointers at the start and end of the array
        l, r = 0, len(nums)-1
        while l <= r:
            # calculate the mid index
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            # else if target > mid, we omit the left half of the array
            elif target > nums[mid]:
                l = mid + 1
            # else if target < mid, we omit the right half of the array
            else:
                r = mid - 1
        return -1
    # Time complexity: O(log(n))
    # Space complexity: O(1)

    # Solution 2: Recursion
    def search2(self, nums: List[int], target: int) -> int:
        def helper(array, target, l, r):
            # specify base case
            if l > r:
                return -1
            # calculate the mid index
            mid = (l+r)//2
            if target == array[mid]:
                return mid
            elif target < array[mid]:
                return helper(array, target, l, mid-1)
            else:
                return helper(array, target, mid+1, r)

        return helper(array=nums, target=target, l=0, r=len(nums)-1)

# Time complexity: O(log(n)), where n is the size of the array
# Space complexity: O(log(n)), as for the recursive approach we need to count the call stacks. 
# Everytime we have a recursive call it is going to take up space. 
# Therefore, implementing the iterative solution is better as it has O(1) space complexity.
