"""
1346. Check If N and Its Double Exist

Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
 

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.
"""

class Solution(object):
    # Solution 1: nested loop
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i != j and arr[i] == arr[j] * 2:
                    return True
        return False
    # time/space complexity: O(n**2)/O(1)
      
      
    # Solution 2: Using enumerate (slightly faster)
    def checkIfExist2(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        for i,x in enumerate(arr):
            for j,y in enumerate(arr):
                if i != j and x == y * 2:
                    return True
        return False
    # time/space complexity: O(n**2)/O(1)     
    
    
    # Solution 3: binary search
    # TO DO
