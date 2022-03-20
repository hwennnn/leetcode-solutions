"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        
        res = []
        queue = deque([root])
        
        while queue:
            n = len(queue)
            curr = []
            
            for _ in range(n):
                node = queue.popleft()
                curr.append(node.val)
                for child in node.children:
                    queue.append(child)
            
            res.append(curr)
        
        return res
            