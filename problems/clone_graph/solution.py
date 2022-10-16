"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        m = {node: Node(node.val)}
        deq = deque([node])
        
        while deq:
            n = deq.popleft()
            for nei in n.neighbors:
                if nei not in m:
                    deq.append(nei)
                    m[nei] = Node(nei.val)
                m[n].neighbors.append(m[nei])
        
        return m[node]