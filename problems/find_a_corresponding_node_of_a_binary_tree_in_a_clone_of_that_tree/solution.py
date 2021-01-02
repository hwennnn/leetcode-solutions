# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def dfs(ori,copy):
            if not ori: return None
            if ori == target: return copy
            
            return dfs(ori.left, copy.left) or dfs(ori.right, copy.right)
        
        return dfs(original, cloned)