"""
1394. Find Lucky Integer in an Array

Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer return -1.
 

Example 1:

Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
"""

# Solution: Hashmap

class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        d = dict()
        out = -1
        
        for v in arr:
            if v in d:
                d[v] += 1
            else:
                d[v] = 1
            
        for k,v in d.items():
            if k == v:
                out = max(out, k)
            
        return out   
      
# Time complexity: O(n)
