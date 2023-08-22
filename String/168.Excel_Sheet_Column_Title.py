"""
168. Excel Sheet Column Title

Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
Example 3:

Input: columnNumber = 701
Output: "ZY"
 

Constraints:

1 <= columnNumber <= 231 - 1
"""

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabet = list(map(chr, range(97, 123)))

        def map_int(num):
            return 26 if num % 26 == 0 else num % 26

        re_columnTitle = []
        while columnNumber > 0:
            re_columnTitle.append(map_int(columnNumber))
            columnNumber = (columnNumber - 1) // 26

        res = ""
        for i in range(len(re_columnTitle) -1, -1, -1):
            for letter in alphabet:
                if ord(letter) - ord("a") == re_columnTitle[i] - 1:
                    res += letter
        return res.upper()

    # Time complexity: O(n), where n is the number of digits in columnNumber
    # Space complexity: O(n), where n is the number of digits in columnNumber
