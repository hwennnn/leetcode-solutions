# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root and root.val > val:
            root.right = self.insertIntoMaxTree(root.right, val)
            return root
        
        node = TreeNode(val)
        node.left = root
        
        return node