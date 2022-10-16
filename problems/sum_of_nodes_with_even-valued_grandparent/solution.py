# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, current, parent, grandparent):
        if not current: return 0
        res = 0
        if grandparent and grandparent.val % 2 == 0:
            res += current.val
        
        return res + self.dfs(current.left, current, parent) + self.dfs(current.right, current, parent)
        
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return self.dfs(root, None, None)