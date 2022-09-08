# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        res = []
        
        def go(node):
            if not node: return
            
            go(node.left)
            res.append(node.val)
            go(node.right)
        
        go(root)
        return res