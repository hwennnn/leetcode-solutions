---
id: minimum-number-of-vertices-to-reach-all-nodes
title: Minimum Number of Vertices to Reach All Nodes
description: Problem Description and Solution for Minimum Number of Vertices to Reach All Nodes
sidebar_label: 1557. Minimum Number of Vertices to Reach All Nodes
sidebar_position: 1557
---

# [1557. Minimum Number of Vertices to Reach All Nodes](https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/)

```py title=minimum-number-of-vertices-to-reach-all-nodes.py
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_degree = [0] * n
        
        for x, y in edges:
            in_degree[y] += 1
        
        res = []
        
        for i in range(n):
            if in_degree[i] == 0:
                res.append(i)
        
        return res
```


