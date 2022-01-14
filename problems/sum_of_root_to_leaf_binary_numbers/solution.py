# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def go(node, curr):
            nonlocal res
            
            if not node: return
            
            v = curr * 2 + node.val
            
            if not node.left and not node.right:
                res += v
                return
            
            go(node.left, v)
            go(node.right, v)
        
        go(root, 0)
        
        return res