# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        value = root.val
        
        def go(node):
            if not node: return True
            
            if node.val != value: return False
            
            return go(node.left) and go(node.right)
        
        return go(root)