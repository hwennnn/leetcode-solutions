# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def go(A, B):
            if not A and not B: return True
            
            if not A or not B: return False
            
            return A.val == B.val and go(A.left, B.left) and go(A.right, B.right)
        
        return go(p, q)