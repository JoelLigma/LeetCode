"""
Counting Sort 1

Comparison Sorting
Quicksort usually has a running time of n*log(n), but is there an algorithm that can sort even faster? In general, this is not possible.
Most sorting algorithms are comparison sorts, i.e. they sort a list just by comparing the elements to one another. 
A comparison sort algorithm cannot beat n*log(n) (worst-case) running time, since n*log(n) represents the minimum number of comparisons needed to know where to place each element. 

Alternative Sorting
Another sorting method, the counting sort, does not require comparison. Instead, you create an integer array whose index range covers the entire range of values
in your array to sort. Each time a value occurs in the original array, you increment the counter at that index. 
At the end, run through your counting array, printing the value of each non-zero valued index that number of times.

Example
arr = [1,1,3,2,1]
All of the values are in the range [0...3] , so create an array of zeros, result = [0,0,0,0]. The results of each iteration follow:

i	arr[i]	result
0  	1	    [0, 1, 0, 0]
1 	1	    [0, 2, 0, 0]
2	  3	    [0, 2, 0, 1]
3   2	    [0, 2, 1, 1]
4 	1	    [0, 3, 1, 1]
The frequency array is [0,3,1,1]. These values can be used to create the sorted array as well: sorted = [1,1,1,2,3].
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    out = [0] * 100 # the solution must contain an array with 100 elements regardless of input size
    for i in range(len(arr)):
        out[arr[i]] += 1
    return out
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
