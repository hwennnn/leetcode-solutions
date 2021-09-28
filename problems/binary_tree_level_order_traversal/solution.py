# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        queue = collections.deque([root])
        res = []
        
        while queue:
            temp = []
            n = len(queue)
            
            for _ in range(n):
                node = queue.popleft()
                temp.append(node.val)
                
                for leaf in (node.left, node.right):
                    if leaf:
                        queue.append(leaf)
            
            res.append(temp)
        
        return res
        