"""
941. Valid Mountain Array

Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true
"""

class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # length of the array must be >= 3
        if len(arr) < 3:
            return False
        
        i = 0
        # we go from left to right to reach a peak
        while i+1 < len(arr) and arr[i] < arr[i+1]:
            i += 1
        
        # once we reached the peak, ensure that it is not the first or last element as that is invalid
        if i == 0 or i == len(arr)-1:
            return False
        
        # next, we go from the peak down to the right
        while i+1 < len(arr) and arr[i] > arr[i+1]:
            i+=1
            
        # if we reach the end of the array with i by passing the conditionals, it is a valid mountain array
        return i == len(arr)-1
# time/space complexity: O(n), O(1)
