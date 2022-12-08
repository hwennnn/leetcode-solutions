---
id: clone-graph
title: Clone Graph
description: Problem Description and Solution for Clone Graph
sidebar_label: 133. Clone Graph
sidebar_position: 133
---

# [133. Clone Graph](https://leetcode.com/problems/clone-graph/)

```py title=clone-graph.py
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
```


