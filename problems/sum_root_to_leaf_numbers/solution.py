# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def go(node, s):
            if not node: return 0
            
            if not node.left and not node.right: return s * 10 + node.val
            
            return go(node.left, s * 10 + node.val) + go(node.right, s * 10 + node.val)
        
        return go(root, 0)