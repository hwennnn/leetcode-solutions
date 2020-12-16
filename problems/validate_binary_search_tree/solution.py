# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root, lessThan = float('inf'), largerThan = float('-inf')) -> bool:
        if not root: return True
        
        if root.val >= lessThan or root.val <= largerThan: return False
        
        return self.isValidBST(root.left, min(lessThan, root.val), largerThan) and self.isValidBST(root.right, lessThan, max(largerThan, root.val)) 