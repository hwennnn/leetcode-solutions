---
id: find-center-of-star-graph
title: Find Center of Star Graph
description: Problem Description and Solution for Find Center of Star Graph
sidebar_label: 1791. Find Center of Star Graph
sidebar_position: 1791
---

# [1791. Find Center of Star Graph](https://leetcode.com/problems/find-center-of-star-graph/)

```py title=find-center-of-star-graph.py
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges)
        mp = collections.defaultdict(int)
        
        for a,b in edges:
            mp[a] += 1
            mp[b] += 1
        
        for key in mp:
            if mp[key] == n:
                return key
        
        return -1
        
```


