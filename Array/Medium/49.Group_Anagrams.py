"""
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        
        for word in strs:
            count = [0] * 26 # number of ch in English alphabet
            for ch in word:
                count[ord(ch) - ord("a")] += 1
            
            # need something hashable here so either tuple or str
            key = tuple(count)
            if key not in d:
                d[key] = [word]
            else:
                d[key] += [word]
        return d.values()

    # Time complexity: O(NK), where N is the size of strs and K is the length of a word in strs
    # Space complexity: O(NK)
