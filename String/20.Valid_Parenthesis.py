class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {"(": ")", "[": "]",  "{": "}"}
        open_brackets = set(["(", "[", "{"])

        for ch in s:
            if ch in open_brackets:
                stack.append(ch)
            elif stack and ch == bracket_map[stack[-1]]:
                stack.pop()
            else:
                return False
        return not stack

# Time complexity: O(n), where n is the size of s
# Space complexity: O(n), where n is the size of the stack in the worst case of opening brackets only
