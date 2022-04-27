"""
1089. Duplicate Zeros

Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
"""

class Solution(object):
    # Solution 1: In-place (preferred)
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        
        i = 0
        while i < len(arr)-1:
            if arr[i] == 0:
                arr.insert(i+1, 0)
                arr.pop(-1)
                i += 1
            i += 1
# Time complexity: O(n)
# Space complexity: O(1)

    
    # Solution 2: Shifting everything to the right as mentioned in the tutorial
    def duplicateZeros2(self, arr):
        temp = []
        for i in range(len(arr)-1, -1, -1):
            if arr[i] == 0 and i != len(arr)-1:
                temp = arr[i+1:-1]
                arr[i+1] = 0
                arr[i+2:] = temp
        
        
    # Solution 3: Avoid shifting
    def duplicateZeros3(self, arr):
        lst = []
        for i in arr:
            lst += [i]
            if i == 0:
                lst += [i]
        arr[:] = lst[:len(arr)]
