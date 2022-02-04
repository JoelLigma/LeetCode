"""
412. Fizz Buzz

Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
 
Example 1:

Input: n = 3
Output: ["1","2","Fizz"]
"""

# Solution:
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        lst = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                lst += ["FizzBuzz"]
            elif i % 3 == 0:
                lst += ["Fizz"]
            elif i % 5 == 0:
                lst += ["Buzz"]
            else:
                lst += [str(i)]   
        return lst
        
# Time complexity: O(n)
# Space complexity: O(1)

"""
FizzBuzzJazz
"""
