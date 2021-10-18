# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        def go(node, parent, depth):
            if not node or len(res) == 2: return
            
            if node.val == x or node.val == y:
                res.append((parent, depth))
            
            go(node.left, node, depth + 1)
            go(node.right, node, depth + 1)
        
        res = []
        go(root, None, 0)
        
        return res[0][0] != res[1][0] and res[0][1] == res[1][1]