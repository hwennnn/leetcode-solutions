---
id: minimum-path-sum
title: Minimum Path Sum
description: Problem Description and Solution for Minimum Path Sum
sidebar_label: 64. Minimum Path Sum
sidebar_position: 64
---

# [64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)

```py title=minimum-path-sum.py
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        for i in range(1, rows):
            grid[i][0] += grid[i - 1][0]
        
        for j in range(1, cols):
            grid[0][j] += grid[0][j - 1]
        
        for i in range(1, rows):
            for j in range(1, cols):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        
        return grid[-1][-1]
```


