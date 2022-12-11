# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -inf

        def go(node):
            nonlocal res
            if not node: return 0

            curr = node.val
            left, right = max(0, go(node.left)), max(0, go(node.right))
            res = max(res, node.val + left + right)

            return node.val + max(0, left, right)
            
        go(root)
        return res