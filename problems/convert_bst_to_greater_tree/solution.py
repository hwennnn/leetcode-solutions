# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    curr = 0
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        if root.right: self.convertBST(root.right)
        root.val = self.curr = self.curr + root.val
        if root.left: self.convertBST(root.left)
        
        return root