# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        
        def dfs(node, curr, path):
            if not node: return
            
            if not node.left and not node.right and curr == targetSum:
                res.append(path)
            
            for leaf in (node.left, node.right):
                if leaf:
                    dfs(leaf, curr + leaf.val, path + [leaf.val])
        
        if root:
            dfs(root, root.val, [root.val])
        
        return res