# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        queue = [root]
        
        while queue:
            
            val = [i.val if i else None for i in queue]
            if val != val[::-1]: return False
            
            queue = [child for i in queue if i for child in (i.left, i.right)]
        return True