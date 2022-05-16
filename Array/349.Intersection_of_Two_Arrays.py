"""
349. Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = set(nums1)        
        out = set()
        for n in nums2:
            if n in s:
                out.add(n)
        return list(out) 
    
    # Time complexity: O(n+m), where n is the size of nums1 and m the size of nums2. O(n) time to convert nums1 to set & O(m) time to loop over nums2. 
    # Space complexity: O(n+m), where n is the size of nums1 and m is the size of nums2
    
    # "lazy" solution
    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1 & set2)    
