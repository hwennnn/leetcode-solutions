---
id: number-of-operations-to-make-network-connected
title: Number of Operations to Make Network Connected
description: Problem Description and Solution for Number of Operations to Make Network Connected
sidebar_label: 1319. Number of Operations to Make Network Connected
sidebar_position: 1319
---

# [1319. Number of Operations to Make Network Connected](https://leetcode.com/problems/number-of-operations-to-make-network-connected/)

```py title=number-of-operations-to-make-network-connected.py
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        m = len(connections)
        
        if m < n - 1: return -1
        
        graph = collections.defaultdict(list)
        visited = [False] * n
        
        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)
        
        def go(node):
            if visited[node]: return 0
            
            visited[node] = True
            
            for nei in graph[node]:
                go(nei)
            
            return 1
        
        return sum(go(node) for node in range(n)) - 1
```


