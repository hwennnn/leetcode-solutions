---
id: largest-local-values-in-a-matrix
title: Largest Local Values in a Matrix
description: Problem Description and Solution for Largest Local Values in a Matrix
sidebar_label: 2373. Largest Local Values in a Matrix
sidebar_position: 2373
---

# [2373. Largest Local Values in a Matrix](https://leetcode.com/problems/largest-local-values-in-a-matrix/)

```py title=largest-local-values-in-a-matrix.py
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = [[0] * (n - 2) for _ in range(n - 2)]
        
        for i in range(n - 2):
            for j in range(n - 2):
                mmax = 0
                for di in range(i, i + 3):
                    for dj in range(j, j + 3):
                        mmax = max(mmax, grid[di][dj])
                
                res[i][j] = mmax
        
        return res
        
```


