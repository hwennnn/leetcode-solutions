# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def go(node):
            nonlocal res
            
            if not node: return 0
            
            left, right = go(node.left), go(node.right)
            coins = left + right + node.val
            res += abs(coins - 1)
            return coins - 1
        
        go(root)
        return res