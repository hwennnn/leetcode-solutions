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
        queue = collections.deque([root])
        
        while queue:
            n = len(queue)
            temp = []
            
            for _ in range(n):
                node = queue.popleft()
                temp.append(node.val)
                
                for leaf in (node.children):
                    if leaf:
                        queue.append(leaf)
            
            res.append(temp)
            
        return res
        