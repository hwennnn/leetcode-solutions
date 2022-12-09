# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def go(node, mmax, mmin):
            if not node: return mmax - mmin

            mmax = max(mmax, node.val)
            mmin = min(mmin, node.val)

            return max(go(node.left, mmax, mmin), go(node.right, mmax, mmin))

        return go(root, root.val, root.val)