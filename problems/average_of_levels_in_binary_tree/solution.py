# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        
        dq = deque([root])
        
        while dq:
            n = len(dq)
            curr = 0
            
            for _ in range(n):
                node = dq.popleft()
                
                curr += node.val
                
                for child in (node.left, node.right):
                    if child:
                        dq.append(child)
            
            res.append(curr / n)
        
        return res