# 226. Invert Binary Tree
# Given the root of a binary tree, invert the tree, and return its root.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        def dfs(root):
            if not root:
                return

            root.left, root.right = root.right, root.left
            
            dfs(root.left)
            dfs(root.right)
            
            return root
        
        return dfs(root)
