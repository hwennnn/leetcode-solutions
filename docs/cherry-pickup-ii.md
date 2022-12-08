---
id: cherry-pickup-ii
title: Cherry Pickup II
description: Problem Description and Solution for Cherry Pickup II
sidebar_label: 1463. Cherry Pickup II
sidebar_position: 1463
---

# [1463. Cherry Pickup II](https://leetcode.com/problems/cherry-pickup-ii/)

```py title=cherry-pickup-ii.py
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        @cache
        def go(row, col1, col2):
            if row == rows: return 0
            
            cherries = grid[row][col1] if col1 == col2 else grid[row][col1] + grid[row][col2]
            res = 0
            
            for nc1 in range(col1 - 1, col1 + 2):
                for nc2 in range(col2 - 1, col2 + 2):
                    if 0 <= nc1 < cols and 0 <= nc2 < cols:
                        res = max(res, go(row + 1, nc1, nc2))
            
            return res + cherries
        
        return go(0, 0, cols - 1)
```


