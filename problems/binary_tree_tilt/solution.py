# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def go(node):
            nonlocal res
            
            if not node: return 0
            
            left = go(node.left)
            right = go(node.right)
            
            res += abs(left - right)
            
            return node.val + left + right
        
        go(root)
        return res