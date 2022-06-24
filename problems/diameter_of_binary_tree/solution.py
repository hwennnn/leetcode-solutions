# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def go(node):
            nonlocal res
            
            if not node: return 0
            
            l, r = go(node.left), go(node.right)
            
            res = max(res, l + r)
            
            return 1 + max(l, r)
        
        go(root)
        
        return res