class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        foundPairs = dict()
        res = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and (nums[i], nums[j]) not in foundPairs and abs(nums[i] - nums[j]) == k:
                    foundPairs[(nums[i], nums[j])] = 1
                    foundPairs[(nums[j], nums[i])] = 1
                    res += 1
                    continue
        return res

        # time complexity: O(N**2), where n is the size of nums
        # space complexity: O(N), where n is the size of foundPairs that scales with the number of pairs
        # In theory the code works but will time out for larger sizes of nums (passing 51/60 cases).
        # We need a smarter approach to avoid this.


       
    def findPairs2(self, nums: List[int], k: int) -> int:
        res = 0
        nums.sort()

        i = 0
        j = 1

        while j < len(nums):
            if abs(nums[i] - nums[j]) < k:
                j += 1
            elif abs(nums[i] - nums[j]) > k:
                i += 1
            elif abs(nums[i] - nums[j]) == k:
                if i > 0 and nums[i] == nums[i - 1]:
                    i += 1
                else: 
                    res += 1
                    i += 1
            
            if i == j:
                j += 1
       
        return res

        # time complexity: O(N logN) + O(N) -> O(N logN), where n is the size of nums
        # space complexity: O(N), where n is the size of foundPairs that scales with the number of pairs


    def findPairs3(self, nums: List[int], k: int) -> int:
        res = 0
        hashMap = dict()

        for i in range(len(nums)):
            if nums[i] in hashMap:
                hashMap[nums[i]] += 1
            else:
                hashMap[nums[i]] = 1


        for key in hashMap:
            if k > 0  and key + k in hashMap:
                res += 1
            elif k == 0 and hashMap[key] > 1:
                res += 1
        return res

    # time complexity: O(N) + O(N) or O(2N) -> O(N), where N is the size of nums and N is the size of the hashMap
    # space complexity: O(N), where N is the size of unique integers in nums -> worst case all unique
