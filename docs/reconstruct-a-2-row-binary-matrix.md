---
id: reconstruct-a-2-row-binary-matrix
title: Reconstruct a 2-Row Binary Matrix
description: Problem Description and Solution for Reconstruct a 2-Row Binary Matrix
sidebar_label: 1253. Reconstruct a 2-Row Binary Matrix
sidebar_position: 1253
---

# [1253. Reconstruct a 2-Row Binary Matrix](https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/)

```py title=reconstruct-a-2-row-binary-matrix.py
class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        cols = len(colsum)
        
        res = [[0]*cols for _ in range(2)]
        
        for j in range(cols):
            if colsum[j] == 2:
                res[0][j] = 1
                res[1][j] = 1
                colsum[j] -= 2
                upper -= 1
                lower -= 1
            
            if upper < 0 or lower < 0: return []
        
        
        for i in range(2):
            for j in range(cols):
                rowsum = upper if i == 0 else lower

                if rowsum > 0 and colsum[j] > 0:
                    res[i][j] = 1
                
                    if i == 0: upper -= 1
                    else: lower -= 1

                    colsum[j] -= 1
                

        return res if upper + lower + sum(colsum) == 0 else []
```


