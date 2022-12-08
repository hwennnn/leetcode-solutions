---
id: minimum-path-cost-in-a-grid
title: Minimum Path Cost in a Grid
description: Problem Description and Solution for Minimum Path Cost in a Grid
sidebar_label: 2304. Minimum Path Cost in a Grid
sidebar_position: 2304
---

# [2304. Minimum Path Cost in a Grid](https://leetcode.com/problems/minimum-path-cost-in-a-grid/)

```py title=minimum-path-cost-in-a-grid.py
class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = float('inf')

        @cache
        def go(i, j):
            if i == rows - 1:
                return grid[i][j]
            
            res = float('inf')

            for k, cost in enumerate(moveCost[grid[i][j]]):
                res = min(res, go(i + 1, k) + cost + grid[i][j])
                
            return res
                
        
        for j in range(cols):
            res = min(res, go(0, j))
        
        return res
        
```


