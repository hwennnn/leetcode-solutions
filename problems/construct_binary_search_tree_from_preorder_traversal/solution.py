# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder: return
        
        val = preorder[0]
        root = TreeNode(val)
        
        left = [v for v in preorder[1:] if v < val]
        right = [v for v in preorder[1+len(left):] if v > val]
        
        root.left = self.bstFromPreorder(left)
        root.right = self.bstFromPreorder(right)
        
        return root
        