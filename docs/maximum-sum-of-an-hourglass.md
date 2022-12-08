---
id: maximum-sum-of-an-hourglass
title: Maximum Sum of an Hourglass
description: Problem Description and Solution for Maximum Sum of an Hourglass
sidebar_label: 2428. Maximum Sum of an Hourglass
sidebar_position: 2428
---

# [2428. Maximum Sum of an Hourglass](https://leetcode.com/problems/maximum-sum-of-an-hourglass/)

```py title=maximum-sum-of-an-hourglass.py
class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        
        for i in range(rows - 2):
            for j in range(1, cols - 1):
                res = max(res, grid[i][j - 1] + grid[i][j] + grid[i][j + 1] + grid[i + 1][j] + grid[i + 2][j - 1] + grid[i + 2][j] + grid[i + 2][j + 1])            
        
        return res
```


