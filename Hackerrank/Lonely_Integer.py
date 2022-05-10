"""
Lonely Integer

Given an array of integers, where all elements but one occur twice, find the unique element.

Example
a = [1,2,3,4,3,2,1]

The unique element is 4.
"""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    d = dict()
    
    for num in a:
        if not num in d:
            d[num] = 1
        elif num in d:
           del d[num]
    return list(d.keys())[0]
            
# Time/space complexity: O(n)/O(n)  
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
