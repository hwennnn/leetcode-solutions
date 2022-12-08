---
id: number-of-provinces
title: Number of Provinces
description: Problem Description and Solution for Number of Provinces
sidebar_label: 547. Number of Provinces
sidebar_position: 547
---

# [547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/)

```py title=number-of-provinces.py
class DSU:
    def __init__(self, n):
        self.graph = list(range(n))

    def find(self, x):
        if self.graph[x] != x:
            self.graph[x] = self.find(self.graph[x])

        return self.graph[x]

    def union(self, x, y):
        ux, uy = self.find(x), self.find(y)
        self.graph[ux] = uy

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def findCircleNum(self, G: List[List[int]]) -> int:
        n = len(G)
        uf = DSU(n)
        
        for node in range(n):
            for nei in range(n):
                if node == nei or G[node][nei] == 0: continue
                
                uf.union(node, nei)
        
        parents = set()
        
        for node in range(n):
            p = uf.find(node)
            parents.add(p)
        
        return len(parents)
```


