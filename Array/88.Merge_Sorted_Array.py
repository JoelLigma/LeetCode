"""
88. Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order. The final sorted array should not be returned by the function, but instead be stored inside
the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are
set to 0 and should be ignored. nums2 has a length of n.

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
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

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # last index of nums1
        last_idx = m+n-1
        
        # merge them in reverse order
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last_idx] = nums1[m-1]
                # since we updated the empty space with an element of nums1, 
                # we decrease the index to the next largest element to continue
                m -= 1
            else:
                nums1[last_idx] = nums2[n-1]
                # same as above but for nums2
                n -= 1

            last_idx -= 1
            
        # lastly, we take care of the edge case where the first element in nums1 is larger than
        # the first element in nums2.
        # The number of leftover elements in nums2 may be >= 1.
        while n > 0:
            nums1[last_idx] = nums2[n-1]
            n -= 1
            last_idx -= 1
            
  # Time/Space complexity analysis: O(n), O(1)
