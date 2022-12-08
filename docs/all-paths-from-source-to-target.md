---
id: all-paths-from-source-to-target
title: All Paths From Source to Target
description: Problem Description and Solution for All Paths From Source to Target
sidebar_label: 797. All Paths From Source to Target
sidebar_position: 797
---

# [797. All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-target/)

```py title=all-paths-from-source-to-target.py
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        res = []
        
        def go(node, path):
            if node == n - 1:
                res.append(path)
                return
            
            for nei in graph[node]:
                go(nei, path + [nei])
        
        go(0, [0])
        
        return res
```


