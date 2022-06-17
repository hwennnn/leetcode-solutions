# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        NO_CAMERA, HAS_CAMERA, NOT_NEEDED = 0, 1, 2
        res = 0
        
        def go(node):
            nonlocal res
            
            if not node: return NOT_NEEDED
            
            l, r = go(node.left), go(node.right)
            
            if l == NO_CAMERA or r == NO_CAMERA:
                res += 1
                return HAS_CAMERA
            elif l == HAS_CAMERA or r == HAS_CAMERA:
                return NOT_NEEDED
            else:
                return NO_CAMERA
        
        if go(root) == NO_CAMERA:
            res += 1
        
        return res