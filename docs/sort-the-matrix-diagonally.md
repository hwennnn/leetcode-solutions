---
id: sort-the-matrix-diagonally
title: Sort the Matrix Diagonally
description: Problem Description and Solution for Sort the Matrix Diagonally
sidebar_label: 1329. Sort the Matrix Diagonally
sidebar_position: 1329
---

# [1329. Sort the Matrix Diagonally](https://leetcode.com/problems/sort-the-matrix-diagonally/)

```py title=sort-the-matrix-diagonally.py
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        mp = collections.defaultdict(list)
        
        for i in range(rows):
            for j in range(cols):
                mp[j-i].append(mat[i][j])

        for key in mp:
            mp[key] = sorted(mp[key], reverse = 1)

        for i in range(rows):
            for j in range(cols):
                mat[i][j] = mp[j-i].pop()
        
        return mat
```


