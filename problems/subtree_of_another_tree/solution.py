# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False
        
        def isSameTree(a, b):
            if not a and not b: return True
            if not a or not b: return False
            
            return a.val == b.val and isSameTree(a.left, b.left) and isSameTree(a.right, b.right)
        
        return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)