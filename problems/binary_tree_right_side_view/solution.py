# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        res = []
        
        queue = deque([root])
        
        while queue:
            n = len(queue)
            count = 0
            
            for i in range(n):
                node = queue.popleft()
                
                for child in (node.left, node.right):
                    if child:
                        queue.append(child)
                    
                if i == n - 1:
                    res.append(node.val)
        
        return res