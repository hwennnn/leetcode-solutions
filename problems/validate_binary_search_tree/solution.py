# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, mmax, mmin):
            if not (mmin < node.val < mmax):
                return False
            
            if node.left and not dfs(node.left, node.val, mmin):
                return False
            
            if node.right and not dfs(node.right, mmax, node.val):
                return False
            
            return True
        
        return dfs(root, inf, -inf)