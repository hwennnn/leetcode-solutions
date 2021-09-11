# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []
        
        def dfs(node, curr, path):
            if not node: return
            
            if not node.left and not node.right and node.val + curr == targetSum:
                self.res.append(path + [node.val])
            
            dfs(node.left, curr + node.val, path + [node.val])
            dfs(node.right, curr + node.val, path + [node.val])
        
        dfs(root, 0, [])
        
        return self.res