# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    val = 0
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root: return root
        
        if root.right: self.convertBST(root.right)
        
        root.val = self.val = root.val + self.val
        
        if root.left: self.convertBST(root.left)
        
        return root