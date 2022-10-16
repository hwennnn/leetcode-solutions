# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = []
        r = 0
        queue = collections.deque([root])
        
        while queue:
            l = []
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                l.append(node.val)
                
                for leaf in (node.left, node.right):
                    if leaf:
                        queue.append(leaf)
            
            if r: l.reverse()
            res.append(l)
            r ^= 1
        
        return res