# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        def dfs(root, curr):
            if not curr: return False
            
            return search(root, curr, k - curr.val) or dfs(root, curr.left) or dfs(root, curr.right)
        
        def search(root, curr, t):
            if not root: return False
            
            return (root.val == t and root.val != curr.val) or (root.val > t and search(root.left, curr, t)) or (root.val < t and search(root.right, curr, t))
        
        return dfs(root, root)