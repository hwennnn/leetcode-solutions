# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @cache
        def rob(node):
            if not node: return 0
            
            rob_this = node.val + not_rob(node.left) + not_rob(node.right)
            not_rob_this = not_rob(node)
            
            return max(rob_this, not_rob_this)
        
        @cache
        def not_rob(node):
            if not node: return 0
            
            return 0 + rob(node.left) + rob(node.right)
        
        return rob(root)