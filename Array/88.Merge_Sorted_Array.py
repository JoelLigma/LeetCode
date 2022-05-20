"""
88. Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order. The final sorted array should not be returned by the function, but instead be stored inside
the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are
set to 0 and should be ignored. nums2 has a length of n.

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]


Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].


Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
"""

# Time/space complexity analysis needs revision!

# Solution 1 sorting the merge array:

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted(nums1[:m] + nums2[:n])
        
# Time/space complexity analysis: O(nlog(n)), O(1)


# Solution 2 while loop:
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    last_idx = n + m - 1        

    while n > 0 and m > 0:
        # we have to use m-1 etc because we have to account for the case where either nums1 or nums2 are empty.
        # if we start with n -= 1, and then indexing the arrays it would skip this while loop with n >= 0 and m >= 0
        # and result in rejection.
        if nums2[n-1] > nums1[m-1]:
            nums1[last_idx] = nums2[n-1]
            n -= 1
        else:
            nums1[last_idx] = nums1[m-1]
            m -= 1
        last_idx -= 1

    # handle the case where nums2 has elements left. This can happen if the values
    # in nums1 are larger than nums2
    while n > 0:
        nums1[last_idx] = nums2[n-1]
        last_idx -= 1
        n -= 1

# Time/Space complexity analysis: O(n), O(1)
