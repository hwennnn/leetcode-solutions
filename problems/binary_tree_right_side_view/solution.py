# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        
        queue = collections.deque([root])
        
        res = []
        
        while queue:
            l = len(queue)
            
            while l > 0:
                node = queue.popleft()
                
                for child in (node.left, node.right):
                    if child:
                        queue.append(child)
                
                l -= 1
                
                if l == 0:
                    res.append(node.val)
        
        return res
        