# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def invert(node):
            if not node: return None
            
            node.left, node.right = invert(node.right), invert(node.left)
            
            return node
        
        return invert(root)