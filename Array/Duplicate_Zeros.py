"""
LeetCode array tutorial question: Duplicate Zeros
"""

class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        # Solution 1: Shifting everything to the right as mentioned in the tutorial
        temp = []
        for i in range(len(arr)-1, -1, -1):
            if arr[i] == 0 and i != len(arr)-1:
                temp = arr[i+1:-1]
                arr[i+1] = 0
                arr[i+2:] = temp
        
        
        # Solution 2: Avoid shifting
        lst = []
        for i in arr:
            lst += [i]
            if i == 0:
                lst += [i]
        arr[:] = lst[:len(arr)]
        
 # Time complexity: O(n)
 # Space complexity: O(n)
