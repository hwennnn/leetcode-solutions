---
id: largest-submatrix-with-rearrangements
title: Largest Submatrix With Rearrangements
description: Problem Description and Solution for Largest Submatrix With Rearrangements
sidebar_label: 1727. Largest Submatrix With Rearrangements
sidebar_position: 1727
---

# [1727. Largest Submatrix With Rearrangements](https://leetcode.com/problems/largest-submatrix-with-rearrangements/)

```py title=largest-submatrix-with-rearrangements.py
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        res = 0
        
        for i in range(1, rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i-1][j]
        
        for row in map(sorted, matrix):
            for j, col in enumerate(row):
                res = max(res, col * (cols - j))
        
        return res
            
```


