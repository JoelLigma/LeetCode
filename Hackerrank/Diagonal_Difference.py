"""
Diagonal Difference

Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix arr is shown below:
arr = [[1,2,3],
       [4,5,6],
       [9,8,9]]
       
The left-to-right diagonal 1 + 5 + 9 = 15. The right to left diagonal 3 + 5 + 9 = 17. Their absolute difference is | 15 - 17| = 2.  
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    r_diag = 0
    l_diag = 0
    last_idx = len(arr)
    
    
    for i in range(n):
        for j in range(n):
            if j == n-1-i:
                r_diag += arr[i][j]
            if i == j:
                l_diag += arr[i][j]

    
    print("right:", r_diag)
    print("left:", l_diag)
    return abs(r_diag - l_diag)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

# Time/space complexity: O(n**2)/O(1)
