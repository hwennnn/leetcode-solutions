# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, lessThan = float('inf'), largerThan = float('-inf')):
            if not node: return True
            
            if node.val >= lessThan or node.val <= largerThan: return False
            
            return dfs(node.left, min(lessThan, node.val), largerThan) and dfs(node.right, lessThan, max(largerThan, node.val))
        
        return dfs(root)