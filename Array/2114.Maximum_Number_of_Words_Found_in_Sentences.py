# 2114. Maximum Number of Words Found in Sentences

# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
# You are given an array of strings sentences, where each sentences[i] represents a single sentence.
# Return the maximum number of words that appear in a single sentence.

# Example 1:

# Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
# Output: 6

# Solution:

class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        
        output = 0
        for i in sentences:
            n = len(i.split())
            if n > output:
                output = n
                
        return output
    
# time/space complexity analysis: O(n)
