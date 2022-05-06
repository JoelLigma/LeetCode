"""
1299. Replace Elements with Greatest Element on Right Side

Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
After doing so, return the array.

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
"""

# Solution 1: The first solution that immediately came to my mind is the following:
class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        if len(arr) == 1:
            arr = [-1]
            return arr
        for i in range(1, len(arr)):
            arr[i-1] = max(arr[i:])
        arr[-1] = -1
        return arr
    # However, this is not optimal because the built-in max() function's time complexity requires O(n) time. 
    # Therefore, the time/space complexity is O(n**2) and O(1)
    # A better solution is the following where we traverse from right to left and keep track of the largest value to the right.
    
    def replaceElements2(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        largest_right_val = -1
        i = len(arr) - 1
        while i >= 0:
            # keep track of current value temporarily
            current_val = arr[i]
            # assign largest value among all values to the right to the current index position
            arr[i] = largest_right_val
            # if current value > largest value to the right
            if current_val > largest_right_val:
                # keep track of that value
                largest_right_val = current_val
            # move from right to left
            i -= 1
        return arr  
      # Space/time complexity: O(n)/O(1) 
