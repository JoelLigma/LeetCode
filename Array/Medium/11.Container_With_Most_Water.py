"""
11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""

class Solution:

    # First attempt: Brute force
    def maxArea(self, height: List[int]) -> int:  
        largest_area = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                factor = min(height[i], height[j])
                area = factor * (j - i)
                largest_area = max(largest_area, area)
        return largest_area

    # Time Limit Exceeded -> 52 / 61 testcases passed as of August 2023


    # Second attempt: 2 Pointers
    def maxArea2(self, height: List[int]) -> int:  
        largest_area = 0
        
        l, r = 0, len(height) - 1
        while l < r:
            area = abs(r - l) * min(height[l], height[r])
            if area > largest_area:
                largest_area = area

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return largest_area
      
    # Time complexity: O(n), where n is the size of the input array
    # Space complexity: O(1)
