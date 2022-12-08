---
id: check-if-matrix-is-x-matrix
title: Check if Matrix Is X-Matrix
description: Problem Description and Solution for Check if Matrix Is X-Matrix
sidebar_label: 2319. Check if Matrix Is X-Matrix
sidebar_position: 2319
---

# [2319. Check if Matrix Is X-Matrix](https://leetcode.com/problems/check-if-matrix-is-x-matrix/)

```py title=check-if-matrix-is-x-matrix.py
class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        
        for i in range(rows):
            for j in range(cols):
                if i == j or i + j == cols - 1:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False
        
        return True
```


