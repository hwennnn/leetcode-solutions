# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def go(a, b):
            if not a: return None
            
            if a is target: return b
            
            return go(a.left, b.left) or go(a.right, b.right)
        
        return go(original, cloned)