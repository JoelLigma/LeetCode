# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# postorder traversal visits left subtree, then right subtree and finally the root

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        out = []
        
        def dfs(node, out):
            if not node:
                return
            
            dfs(node.left, out)
            dfs(node.right, out)
            out.append(node.val)
            
        dfs(root, out)
        
        return out
