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

# Solution 1: Appending to list
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

If we try to solve this with the previous approach the program would have too many conditions to check:

- Divisible by 3
- Divisible by 5
- Divisible by 7
- Divisible by 3 and 5
- Divisible by 3 and 7
- Divisible by 7 and 3
- Divisible by 3 and 5 and 7
- Not divisible by 3 or 5 or 7.

This way if the FizzBuzz mappings increase, the conditions would grow exponentially.
"""

# Solution 2: String concatenation & add to output list. 
# Can be extended to FizzBuzzJazz while avoiding the problem of the exponential growth of the number of conditions which have to be checked.
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        output = []
        
        for i in range(1, n+1):
            temp_str = ""
            
            if i % 3 == 0:
                temp_str += "Fizz"
            if i % 5 == 0:
                temp_str += "Buzz"
            elif i % 7 == 0:
                temp_str += "Jazz"
            if not temp_str:
                temp_str += str(i)
                
            output += [temp_str]
            
        return output
       
# Time complexity: O(n)
# Space complexity: O(1)


# Solution 3: Hashmap
# This way we can add/delete mappings in the hash table and not worry about changing the code. 
# Advantage: It is easier to maintain
# Disadvantage: It seems it is slower than the previous solutions

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        output = []
        
        d = {
            3: "Fizz",
            5: "Buzz"
            #7: "Jazz"
        }
        
        for i in range(1, n+1):
            temp_str = ""
            
            for key in d.keys():
                if i % key == 0:
                    temp_str += d[key]
            if not temp_str:
                temp_str = str(i)
                
            output += [temp_str]
            
        return output

# Time complexity: O(n)
# Space complexity: O(1)
