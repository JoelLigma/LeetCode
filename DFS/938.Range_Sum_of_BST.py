# 938. Range Sum of BST
# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        
        lst = []
        
        def dfs(root, lst):
            
            if not root:
                return lst
            if (root.val >= low) & (root.val <=high):
                lst += [root.val]
                
            dfs(root.left, lst)
            dfs(root.right, lst)
                
            return lst
                                
        return sum(dfs(root, lst))
