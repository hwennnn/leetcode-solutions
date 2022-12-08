---
id: lucky-numbers-in-a-matrix
title: Lucky Numbers in a Matrix
description: Problem Description and Solution for Lucky Numbers in a Matrix
sidebar_label: 1380. Lucky Numbers in a Matrix
sidebar_position: 1380
---

# [1380. Lucky Numbers in a Matrix](https://leetcode.com/problems/lucky-numbers-in-a-matrix/)

```py title=lucky-numbers-in-a-matrix.py
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        r,c = len(matrix), len(matrix[0])
        col = [0] * c
        # calculate max col
        for i in range(c):
            col[i] = max([matrix[j][i] for j in range(r)])
        
        res = []
        for i in range(r):
            for j in range(c):
                if min(matrix[i]) == matrix[i][j] and col[j] == matrix[i][j]:
                    res.append(matrix[i][j])
                
        return res
```


