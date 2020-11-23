# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        cache = {}
        
        def rob_this(node):
            if not node: return 0
            
            if node in cache: return cache[node]
            
            rob = node.val + not_rob_this(node.left) + not_rob_this(node.right)
            
            not_rob = 0 + rob_this(node.left) + rob_this(node.right)
            
            cache[node] = max(rob, not_rob)
            
            return cache[node]
            
        
        def not_rob_this(node):
            if not node: return 0
            
            return 0 + rob_this(node.left) + rob_this(node.right)
        
        
        return rob_this(root)
            
            