---
id: redundant-connection
title: Redundant Connection
description: Problem Description and Solution for Redundant Connection
sidebar_label: 684. Redundant Connection
sidebar_position: 684
---

# [684. Redundant Connection](https://leetcode.com/problems/redundant-connection/)

```py title=redundant-connection.py
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        
        parent = [i for i in range(n)]
        
        def ufind(x):
            if parent[x] != x:
                parent[x] = ufind(parent[x])
            
            return parent[x]
        
        def uunion(x, y):
            px = ufind(x)
            py = ufind(y)
            
            parent[px] = py
        
        for a, b in edges:
            a -= 1; b -= 1
            
            if ufind(a) == ufind(b):
                return [a + 1, b + 1]
            
            uunion(a, b)
```


