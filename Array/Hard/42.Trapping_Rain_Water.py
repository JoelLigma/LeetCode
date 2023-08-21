"""
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l_max_height, r_max_height = [0] * n, [0] * n
        water_trapped = 0
    
        for i in range(1, n):
            l_max_height[i] = max(l_max_height[i - 1], height[i - 1])
            r_max_height[n - i - 1] =  max(r_max_height[n - i], height[n - i])     

        for i in range(n):
            diff = height[i] - min(l_max_height[i], r_max_height[i])
            if diff < 0:
                water_trapped += diff * -1

        return water_trapped

# Time complexity: O(n), where n is the size of height
# Space complexity: O(n), where n is the size of height
