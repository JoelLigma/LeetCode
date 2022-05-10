"""
Time Conversion

Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example

s = "12:01:00PM"
Return '12:01:00'.

s = "12:01:00AM"
Return '00:01:00'.
"""


import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    
    out = ""
    current_str = s[:-2].split(":")
    time_format = s[-2:]
    if time_format == "PM" and int(current_str[0]) != 12:
        current_str[0] = int(current_str[0]) + 12
    elif time_format == "AM" and int(current_str[0]) == 12:
        current_str[0] = "00"
    return f"{current_str[0]}:{current_str[1]}:{current_str[2]}"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
