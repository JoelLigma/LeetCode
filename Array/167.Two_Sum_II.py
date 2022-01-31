"""
167. Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
"""

# Solution 1:
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()
        for i, v in enumerate(numbers):
            if target - v in d:
                return [d[target - v]+1, i+1]
            d[v] = i
            
# Space/time complexity analysis: Space: O(n) & Time: O(n) 
# adding 1 to the indices is O(1) but dictionary may scale with input array size

# Solution 2: Two-pointer
"""
Two-pointer solution

Explanation:

- there is only one solution
- Long explanation: array is sorted, thus if the current pair of integers > target, we know that we must reduce the right pointer to get a
  smaller number to ultimately get closer to the result. Likewise, if the current pair of intergers < target, we know that we must increase 
  the left pointer to get a larger integer and reach the result.
- In short: increase in left pointer == increase the sum, decrease in right pointer == decrease the sum

Time complexity in the worst case: O(n)
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers)-1
        while l < r:  
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
