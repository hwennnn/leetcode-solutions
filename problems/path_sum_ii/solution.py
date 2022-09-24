# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def go(node, curr, path):
            if not node: return

            if not node.left and not node.right and curr + node.val == targetSum:
                res.append(path + [node.val])
                return
            
            go(node.left, curr + node.val, path + [node.val])
            go(node.right, curr + node.val, path + [node.val])
        
        go(root, 0, [])
        return res