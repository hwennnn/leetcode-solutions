# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        
        def go(node):
            nonlocal res
            
            if not node: return 0
            
            l, r = go(node.left), go(node.right)
            
            if abs(l - r) > 1:
                res = False
            
            return 1 + max(l, r)
        
        go(root)
        
        return res