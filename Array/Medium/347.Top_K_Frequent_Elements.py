"""
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
"""
import random

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = dict()

        for i,v in enumerate(nums):
            if v in hashMap:
                hashMap[v] += 1
            else:
                hashMap[v] = 1
        
        unique = list(hashMap.keys())

        def partition(l, r, pivot) -> int:
            """
            Lomuto's Partition Scheme
            """
            pivot_freq = hashMap[unique[pivot]]
            # step 1: move pivot to the end
            unique[pivot], unique[r] = unique[r], unique[pivot]

            # step 2: move all less frequent elements to the left
            store_idx = l
            while l < r:
                if hashMap[unique[l]] < pivot_freq:
                    unique[store_idx], unique[l] = unique[l], unique[store_idx]
                    store_idx += 1
                l += 1

            # step 3: in the end we move pivot to its final place
            unique[store_idx], unique[r] = unique[r], unique[store_idx]

            return store_idx

        # quick select
        def quickSelect(l, r, k) -> None:
            """
            Hoare's selection algorithm. Sort list in ascending order.
            """
            # base case
            if l == r:
                return

            # select a random pivot (must be random otherwise can lead to O(N**2) time complexity)
            pivot = random.randint(l, r)

            # find the pivot position in the list
            pivot = partition(l, r, pivot)

            # if pivot is in its final sorted position
            if k == pivot:
                return
            # elif k < pivot go left
            elif k < pivot:
                quickSelect(l, pivot - 1, k)
            # else go right
            else:
                quickSelect(pivot + 1, r, k)
        
        # sort unique keys in ascending order and return the k most frequent ones
        n = len(unique)
        quickSelect(0, n - 1, n - k)
        return unique[n - k:]

# Time complexity: O(N) in the average case using random pivots. We apply recursion on only one half of the partition. 
# In the worst-case of constantly bad chosen pivots, the problem is not divided by half at each step, it becomes just
# one element less, that leads to O(N2) time complexity. This can happen for if we fix the pivot at e.g. the right-most element
# Space complexity: O(N) to store the elements in the hashmap
