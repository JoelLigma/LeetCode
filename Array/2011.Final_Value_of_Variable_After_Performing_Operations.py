# 2011. Final Value of Variable After Performing Operations

# There is a programming language with only four operations and one variable X:

# ++X and X++ increments the value of the variable X by 1.
# --X and X-- decrements the value of the variable X by 1.
# Initially, the value of X is 0.

# Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.

# Example 1:

# Input: operations = ["--X","X++","X++"]
# Output: 1

class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        return sum(1 if "+" in i[1] else -1 for i in operations)
    
# time complexity: O(n)
