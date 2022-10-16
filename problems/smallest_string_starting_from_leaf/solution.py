# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res = None
        
        def dfs(node, path):
            if not node: return
            
            if not node.left and not node.right:
                nonlocal res
                path = chr(ord('a') + node.val) + path
                if res is None:
                    res = path
                else:
                    res = min(res, path)
                return
            
            dfs(node.left, chr(ord('a') + node.val) + path)
            dfs(node.right, chr(ord('a') + node.val) + path)
        
        dfs(root, "")
        
        return res