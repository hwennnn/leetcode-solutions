---
id: minimum-score-of-a-path-between-two-cities
title: Minimum Score of a Path Between Two Cities
description: Problem Description and Solution for Minimum Score of a Path Between Two Cities
sidebar_label: 2492. Minimum Score of a Path Between Two Cities
sidebar_position: 2492
---

# [2492. Minimum Score of a Path Between Two Cities](https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/)

```py title=minimum-score-of-a-path-between-two-cities.py
class Solution:
    def minScore(self, N: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        for a, b, dist in roads:
            graph[a].append((b, dist))
            graph[b].append((a, dist))
            
        res = inf
        
        stack = [1]
        visited = set(stack)
        
        while stack:
            node = stack.pop()
            
            for nei, dist in graph[node]:
                res = min(res, dist)
                
                if nei in visited: continue
                
                visited.add(nei)
                stack.append(nei)
            
        return res
```


