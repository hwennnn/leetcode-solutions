---
id: longest-cycle-in-a-graph
title: Longest Cycle in a Graph
description: Problem Description and Solution for Longest Cycle in a Graph
sidebar_label: 2360. Longest Cycle in a Graph
sidebar_position: 2360
---

# [2360. Longest Cycle in a Graph](https://leetcode.com/problems/longest-cycle-in-a-graph/)

```py title=longest-cycle-in-a-graph.py
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        visited = [False] * n
        res = -1
        
        for node in range(n):
            dist = {}
            d = 0
            
            while node != -1 and not visited[node]:
                visited[node] = True
                dist[node] = d
                node = edges[node]
                d += 1
            
            if node != -1 and node in dist:
                res = max(res, d - dist[node])
        
        return res
        
```


