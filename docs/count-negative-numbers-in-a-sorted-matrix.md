---
id: count-negative-numbers-in-a-sorted-matrix
title: Count Negative Numbers in a Sorted Matrix
description: Problem Description and Solution for Count Negative Numbers in a Sorted Matrix
sidebar_label: 1351. Count Negative Numbers in a Sorted Matrix
sidebar_position: 1351
---

# [1351. Count Negative Numbers in a Sorted Matrix](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/)

```py title=count-negative-numbers-in-a-sorted-matrix.py
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] < 0:
                    res += 1
        
        return res
```


