# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dq = deque([root])
        level = 0
        
        while dq:
            n = len(dq)
            currLevel = []
            
            for _ in range(n):
                node = dq.popleft()
                currLevel.append(node)
                
                for child in filter(None, (node.left, node.right)):
                    dq.append(child)
            
            if level % 2 == 1:
                vals = [node.val for node in currLevel][::-1]
                for node, val in zip(currLevel, vals):
                    node.val = val
            
            level += 1
            
        return root