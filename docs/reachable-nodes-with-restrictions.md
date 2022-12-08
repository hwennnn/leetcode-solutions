---
id: reachable-nodes-with-restrictions
title: Reachable Nodes With Restrictions
description: Problem Description and Solution for Reachable Nodes With Restrictions
sidebar_label: 2368. Reachable Nodes With Restrictions
sidebar_position: 2368
---

# [2368. Reachable Nodes With Restrictions](https://leetcode.com/problems/reachable-nodes-with-restrictions/)

```py title=reachable-nodes-with-restrictions.py
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        res = 0
        R = set(restricted)
        visited = set()
        G = defaultdict(list)
        
        for a, b in edges:
            G[a].append(b)
            G[b].append(a)
        
        def dfs(node):
            visited.add(node)
            
            for nei in G[node]:
                if nei not in R and nei not in visited:
                    dfs(nei)
        
        dfs(0)
        return len(visited)
```


