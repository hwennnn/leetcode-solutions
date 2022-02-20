# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        res = []
        
        def go(node, depth, parent):
            if not node: return
            
            if node.val == x or node.val == y:
                res.append((depth, parent))
            
            go(node.left, depth + 1, node.val)
            go(node.right, depth + 1, node.val)
        
        go(root, 0, None)
        
        return len(res) == 2 and res[0][0] == res[1][0] and res[0][1] != res[1][1]
                