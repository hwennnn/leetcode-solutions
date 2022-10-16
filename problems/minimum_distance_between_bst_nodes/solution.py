# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        A = []
        
        def dfs(node):
            if not node: return
            
            dfs(node.left)
            A.append(node.val)
            dfs(node.right)
        
        dfs(root)
        
        return min(b - a for a, b in zip(A, A[1:]))