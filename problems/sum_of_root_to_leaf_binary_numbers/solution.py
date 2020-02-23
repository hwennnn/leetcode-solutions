# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode,val=0) -> int:
        if not root: return 0
        val = val * 2 + root.val
        if root.left == root.right: return val
        return self.sumRootToLeaf(root.left, val) + self.sumRootToLeaf(root.right, val)