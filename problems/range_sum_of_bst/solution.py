# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def go(node):
            if not node: return 0
            
            return (node.val if low <= node.val <= high else 0) + go(node.left) + go(node.right)
            
        
        return go(root)