---
id: reorder-routes-to-make-all-paths-lead-to-the-city-zero
title: Reorder Routes to Make All Paths Lead to the City Zero
description: Problem Description and Solution for Reorder Routes to Make All Paths Lead to the City Zero
sidebar_label: 1466. Reorder Routes to Make All Paths Lead to the City Zero
sidebar_position: 1466
---

# [1466. Reorder Routes to Make All Paths Lead to the City Zero](https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/)

```py title=reorder-routes-to-make-all-paths-lead-to-the-city-zero.py
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = [False] * n
        graph = defaultdict(list)
        
        for x, y in connections:
            graph[x].append(y)
            graph[y].append(-x)
        
        def go(node):
            visited[node] = True
            res = 0
            
            for nei in graph[node]:
                if not visited[abs(nei)]:
                    visited[abs(nei)] = True
                    res += go(abs(nei)) + int(nei > 0)
            
            return res
        
        return go(0)
```


