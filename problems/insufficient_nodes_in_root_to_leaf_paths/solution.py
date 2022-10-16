# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        if root.left == root.right:
            return None if root.val < limit else root
        
        if root.left:
            root.left = self.sufficientSubset(root.left, limit - root.val)
        
        if root.right:
            root.right = self.sufficientSubset(root.right, limit - root.val)
        
        return root if root.left or root.right else None