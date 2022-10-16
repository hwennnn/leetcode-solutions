# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isSame(left, right):
            if not left or not right: return left == right
            
            if left.val != right.val: return False
            
            return isSame(left.left, right.right) and isSame(left.right, right.left)
        
        return not root or isSame(root.left, root.right)