"""
Debugging Challenge: Zig Zag Sequence

In this challenge, the task is to debug the existing code to successfully execute all provided test files.

Given an array of n distinct integers, transform the array into a zig zag sequence by permuting the array elements.
A sequence will be called a zig zag sequence if the first k elements in the sequence are in increasing order and the last k elements are in decreasing order,
where k = (n+1)/2. You need to find the lexicographically smallest zig zag sequence of the given array.

Example.
a = [2,3,5,1,4]

Now if we permute the array as [1,4,5,3,2], the result is a zig zag sequence.

Debug the given function findZigZagSequence to return the appropriate zig zag sequence for the given input array.

Note: You can modify at most three lines in the given code. You cannot add or remove lines of code.

"""

def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2) - 1 # need to subtract one to reach the middle of the array
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2 # 2. the last element has already been swapped so decrement by 2 instead of 1
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1 # 3. We have to decrement this as otherwise it will loop endlessly

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)
