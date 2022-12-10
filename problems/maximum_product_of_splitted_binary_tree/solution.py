# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        M = 10 ** 9 + 7
        res = 0

        def dfs(node):
            if not node: return 0
            return node.val + dfs(node.left) + dfs(node.right)

        total = dfs(root)
        
        def dfs2(node):
            nonlocal res

            if not node: return 0

            curr = node.val + dfs2(node.left) + dfs2(node.right)
            remaining = total - curr

            res = max(res, (curr * remaining))

            return curr
        
        dfs2(root)
        return res % M