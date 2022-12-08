---
id: equal-row-and-column-pairs
title: Equal Row and Column Pairs
description: Problem Description and Solution for Equal Row and Column Pairs
sidebar_label: 2352. Equal Row and Column Pairs
sidebar_position: 2352
---

# [2352. Equal Row and Column Pairs](https://leetcode.com/problems/equal-row-and-column-pairs/)

```py title=equal-row-and-column-pairs.py
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        R = Counter()
        C = Counter()
        
        for row in grid:
            R[tuple(row)] += 1
        
        for col in zip(*grid):
            C[tuple(col)] += 1
        
        res = 0
        for row, cnt in R.items():
            res += cnt * C[row]
        
        return res
```


