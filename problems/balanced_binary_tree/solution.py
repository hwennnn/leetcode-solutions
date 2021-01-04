# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        def dfs(root):
            if not root: return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            if left == -1 or right == -1 or abs(left - right) > 1: return -1
            
            return 1 + max(left, right)
        
        return dfs(root) != -1