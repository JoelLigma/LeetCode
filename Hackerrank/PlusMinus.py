"""
Question: Plus Minus

Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.
Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to 10^-4 are acceptable.

Example
arr = [1,1,0,-1,-1]
There are n=5 elements, two positive, two negative and one zero. Their ratios are 2/5, 1/5 and 2/5. Results are printed as:

0.400000
0.400000
0.200000
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos = 0
    neg = 0
    z = 0
    for num in arr:
        if num > 0:
            pos += 1
        elif num == 0:
            z += 1
        else:
            neg +=1
    
    sys.stdout.write(str(round(pos/len(arr),6))+"\n"+\
                     str(round(neg/len(arr),6))+"\n"+\
                     str(round(z/len(arr),6))
                    )
    
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
    
    
# Time/space complexity: O(n),O(1)
