# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.ans = 0
        
        def go(node):
            if not node: return 0
            
            left, right = go(node.left), go(node.right)
            self.ans += abs(left-right)
            
            return node.val + left + right
        
        go(root)
        return self.ans
            