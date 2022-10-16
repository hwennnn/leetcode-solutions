# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        
        q = collections.deque([[root,1]])
        
        while q:
            node, level = q.popleft()
            
            if node:
                if not node.left and not node.right:
                    return level
                
                for n in (node.left,node.right):
                    if n:
                        q.append([n, level + 1])