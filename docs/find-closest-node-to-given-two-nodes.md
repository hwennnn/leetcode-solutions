---
id: find-closest-node-to-given-two-nodes
title: Find Closest Node to Given Two Nodes
description: Problem Description and Solution for Find Closest Node to Given Two Nodes
sidebar_label: 2359. Find Closest Node to Given Two Nodes
sidebar_position: 2359
---

# [2359. Find Closest Node to Given Two Nodes](https://leetcode.com/problems/find-closest-node-to-given-two-nodes/)

```py title=find-closest-node-to-given-two-nodes.py
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        
        def gen(node):
            dist = [inf] * n
            visited = [False] * n
            d = 0
            
            while node != -1 and not visited[node]:
                visited[node] = True
                dist[node] = d
                d += 1
                node = edges[node]
            
            return dist

        dist1 = gen(node1)
        dist2 = gen(node2)
        
        res = inf
        index = 0

        for i, (a, b) in enumerate(zip(dist1, dist2)):
            s = max(a, b)
            if s < res:
                res = s
                index = i
        
        return -1 if res == inf else index
        
```


