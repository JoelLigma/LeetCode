"""
278. First Bad Version

You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version.
You should minimize the number of calls to the API.


Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
"""

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    # Solution 1: Iterative 
    def firstBadVersion(self, n: int) -> int:
        for i in range(1,n+1):
            if isBadVersion(i):
                return i
    # Time complexity: O(n)
    # Space complexity: O(1)
    # However, we were asked to minimise the API calls, and since the array is sorted, we can use binary search
    
    # Solution 2: Binary Search (preferred)
    def firstBadVersion2(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            mid = (l+r) // 2
            if isBadVersion(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l     
    # Time complexity: O(log(n))
    # Space complexity: O(1)
