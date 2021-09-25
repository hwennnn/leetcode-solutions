# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2: return None
        
        if root1:
            v1, l1, r1 = root1.val, root1.left, root1.right
        else:
            v1, l1, r1 = 0, None, None
        
        if root2:
            v2, l2, r2 = root2.val, root2.left, root2.right
        else:
            v2, l2, r2 = 0, None, None
        
        node = TreeNode(v1 + v2)
        node.left = self.mergeTrees(l1, l2)
        node.right = self.mergeTrees(r1, r2)
        
        return node