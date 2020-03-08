# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        self.ans = 0
        
        def depth(p):
            if not p: return 0
            
            left,right = depth(p.left), depth(p.right)
            self.ans = max(self.ans, left+right)
            
            return 1 + max(left, right)

            
        depth(root)
        
        return self.ans