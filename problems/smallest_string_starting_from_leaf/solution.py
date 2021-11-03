# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        if not root: return ''
        
        def go(node, s):
            nonlocal res
            
            s += chr(ord('a') + node.val)
            
            if not node.left and not node.right:
                if res is None:
                    res = s[::-1]
                else:
                    res = min(res, s[::-1])
            
            if node.left:
                go(node.left, s)
            
            if node.right:
                go(node.right, s)
            
        res = None
        go(root, '')
        
        return res