---
id: cyclically-rotating-a-grid
title: Cyclically Rotating a Grid
description: Problem Description and Solution for Cyclically Rotating a Grid
sidebar_label: 1914. Cyclically Rotating a Grid
sidebar_position: 1914
---

# [1914. Cyclically Rotating a Grid](https://leetcode.com/problems/cyclically-rotating-a-grid/)

```py title=cyclically-rotating-a-grid.py
class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        
        for r in range(min(rows, cols) // 2):
            i = j = r
            vals = []
            
            for jj in range(j, cols - j - 1):
                vals.append(grid[i][jj])
            
            for ii in range(i, rows - i - 1):
                vals.append(grid[ii][cols - j - 1])
            
            for jj in range(cols - j - 1, j, -1):
                vals.append(grid[rows - i - 1][jj])
            
            for ii in range(rows - i - 1, i, -1):
                vals.append(grid[ii][j])
            
            kk = k % len(vals)
            vals = vals[kk:] + vals[:kk]
            x = 0
            
            for jj in range(j, cols - j - 1):
                grid[i][jj] = vals[x]; x += 1
            
            for ii in range(i, rows - i - 1):
                grid[ii][cols - j - 1] = vals[x]; x += 1
            
            for jj in range(cols - j - 1, j, -1):
                grid[rows - i - 1][jj] = vals[x]; x += 1
            
            for ii in range(rows - i - 1, i, -1):
                grid[ii][j] = vals[x]; x += 1
        
        return grid
            
```


