---
id: spiral-matrix
title: Spiral Matrix
description: Problem Description and Solution for Spiral Matrix
sidebar_label: 54. Spiral Matrix
sidebar_position: 54
---

# [54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)

```py title=spiral-matrix.py
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        rows, cols = len(matrix), len(matrix[0])
        rowStart, rowEnd = 0, rows - 1
        colStart, colEnd = 0, cols - 1
        
        while len(res) < rows * cols:
            # traverse right
            i = colStart
            while len(res) < rows * cols and i <= colEnd:
                res.append(matrix[rowStart][i])
                i += 1
            rowStart += 1
            
            # traverse down
            i = rowStart
            while len(res) < rows * cols and i <= rowEnd:
                res.append(matrix[i][colEnd])
                i += 1
            colEnd -= 1
            
            # traverse left
            i = colEnd
            while len(res) < rows * cols and i >= colStart:
                res.append(matrix[rowEnd][i])
                i -= 1
            rowEnd -= 1
        
            # traverse up
            i = rowEnd
            while len(res) < rows * cols and i >= rowStart:
                res.append(matrix[i][colStart])
                i -= 1
            colStart += 1
                
        
        return res
```


