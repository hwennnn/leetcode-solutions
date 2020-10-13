# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def count(root, v):
            if not root: return 0
            
            m = max(root.val, v)
            
            return (root.val >= v) + count(root.left, max(root.val,v)) + count(root.right, max(root.val, v))
        
        return count(root, root.val)