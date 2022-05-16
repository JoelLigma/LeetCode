"""
350. Intersection of Two Arrays II

Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = dict()
        for n in nums1:
            if not n in d:
                d[n] = 1
            else:
                d[n] += 1
        
        out = []
        for n in nums2:
            if n in d and d[n] >= 1:
                out += [n]
                d[n] -= 1 #!!! decrement by one if we have appended an element to the list
        return out
    
    # time complexity: O(n+m) -> linear, where n is the size of nums1 and m the size of nums2
    # space complexity: O(n+m) -> linear, where n is the size of dict and m the size of the output list
