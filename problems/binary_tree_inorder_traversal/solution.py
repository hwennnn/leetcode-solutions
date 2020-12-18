# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        
        def helperR(root):
            if not root: return
            
            helperR(root.left)
            res.append(root.val)
            helperR(root.right)
            
        helperR(root)
        
        return res