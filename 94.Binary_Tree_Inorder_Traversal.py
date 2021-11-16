# 94. Binary Tree Inorder Traversal
# Given the root of a binary tree, return the inorder traversal of its nodes' values.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# in-order dfs left, root, right

class Solution:
       
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:    
        
        output = []
        
        def dfs(root, output):
            # base case
            if not root:
                return output
            
            # traversing the tree starting with left
            if root.left:
                dfs(root.left, output)
                
            # then add root node to output
            output += [root.val]
   
            # finally, traverse the right side
            if root.right:
                dfs(root.right, output)

            return output
                
        return dfs(root, output)