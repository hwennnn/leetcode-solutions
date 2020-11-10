# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root):

        if not root: return 0
        return self.helper(root, root.val, root.val)
    
    def helper(self, node, high, low):
        if not node:
            return high - low
        high = max(high, node.val)
        low = min(low, node.val)
        return max(self.helper(node.left, high, low), self.helper(node.right,high,low))