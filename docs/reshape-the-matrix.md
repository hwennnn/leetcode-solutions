---
id: reshape-the-matrix
title: Reshape the Matrix
description: Problem Description and Solution for Reshape the Matrix
sidebar_label: 566. Reshape the Matrix
sidebar_position: 566
---

# [566. Reshape the Matrix](https://leetcode.com/problems/reshape-the-matrix/)

```py title=reshape-the-matrix.py
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        if rows * cols != c * r: return mat
        
        res = [[0] * c for _ in range(r)]
        index = 0
        
        for i in range(rows):
            for j in range(cols):
                res[index // c][index % c] = mat[i][j]
                index += 1
        
        return res
```


