"""
1207. Unique Number of Occurrences

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
"""

class Solution:

    # first naive solution
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashMap = dict()

        for i,v in enumerate(arr):
            if v in hashMap:
                hashMap[v] += 1
            else: 
                hashMap[v] = 1
        
        freqHashMap = dict()
        for i,v in enumerate(list(hashMap.values())):
            if v in freqHashMap:
                return False
            else:
                freqHashMap[v] = 1
        return True

    # better solution using set
    def uniqueOccurrences2(self, arr: List[int]) -> bool:
        hashMap = dict()

        for i,v in enumerate(arr):
            if v in hashMap:
                hashMap[v] += 1
            else: 
                hashMap[v] = 1        
        return len(set(hashMap.values())) == len(hashMap)

# Time complexity: O(n), where n is the size of arr
# Space complexity: O(n), where n is the size of arr. Worst case all uniques
