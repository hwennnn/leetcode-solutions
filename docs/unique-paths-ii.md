---
id: unique-paths-ii
title: Unique Paths II
description: Problem Description and Solution for Unique Paths II
sidebar_label: 63. Unique Paths II
sidebar_position: 63
---

# [63. Unique Paths II](https://leetcode.com/problems/unique-paths-ii/)

```py title=unique-paths-ii.py
class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[0] * cols for _ in range(rows)]
        dp[0][0] = 1 - grid[0][0]
        
        for j in range(1, cols):
            dp[0][j] += dp[0][j - 1] * (1 - grid[0][j])
        
        for i in range(1, rows):
            dp[i][0] += dp[i - 1][0] * (1 - grid[i][0])
            
        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] += (dp[i - 1][j] + dp[i][j - 1]) * (1 - grid[i][j])
        
        return dp[-1][-1]
```


