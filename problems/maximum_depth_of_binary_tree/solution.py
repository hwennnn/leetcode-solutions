# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        
        deq = collections.deque([root])
        level = 0
        
        while deq:
            n = len(deq)
            level += 1
            
            while n > 0:
                node = deq.popleft()
                for leaves in (node.left, node.right):
                    if leaves:
                        deq.append(leaves)
                n -= 1
            
        
        return level