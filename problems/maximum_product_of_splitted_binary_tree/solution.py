# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def calculateTotal(node):
            if not node: return 0
            
            return node.val + calculateTotal(node.left) + calculateTotal(node.right)
        
        total = calculateTotal(root)

        def dfs(node):
            if not node: return 0

            curr = node.val + dfs(node.left) + dfs(node.right)
            self.res = max(self.res, (total - curr) * curr)
            
            return curr

        dfs(root)
        
        return self.res % (10 ** 9 + 7)
        
        