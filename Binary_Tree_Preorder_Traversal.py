# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# preorder traversal visits the root node first

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        out = []
        
        def dfs(node, out):
            if not node:
                return
            out.append(node.val)
            dfs(node.left, out)
            dfs(node.right, out)
            
        dfs(root, out)
        
        return out
