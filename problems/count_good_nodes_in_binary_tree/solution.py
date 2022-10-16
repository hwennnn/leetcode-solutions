# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, mmax):
            if not node: return 0
            mmax = max(mmax, node.val)
            
            return (node.val >= mmax) + dfs(node.left, mmax) + dfs(node.right, mmax)
        
        return dfs(root, root.val)