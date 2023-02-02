# 2535. Difference Between Element Sum and Digit Sum of an Array
# Easy

# You are given a positive integer array nums.

# The element sum is the sum of all the elements in nums.
# The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
# Return the absolute difference between the element sum and digit sum of nums.

# Note that the absolute difference between two integers x and y is defined as |x - y|.

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:

        # digit sum -> sum of all digits of numbers in array
        # element sum -> sum of elements in array

        digit = 0
        digitSum = 0
        elSum = 0
        for i in range(len(nums)):
            elSum += nums[i]
            digit = str(nums[i])
            [digitSum:= digitSum + int(n) for n in digit]

        return abs(elSum - digitSum)
  
  # 1 <= nums[i] <= 2000 and 1 <= nums.length <= 2000
  # time/space complexity: O(n) as the complexity increases with the size of the array. Digit is capped at 4 in this example. / space: O(1)
