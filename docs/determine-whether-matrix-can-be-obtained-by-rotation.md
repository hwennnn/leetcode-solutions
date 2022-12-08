---
id: determine-whether-matrix-can-be-obtained-by-rotation
title: Determine Whether Matrix Can Be Obtained By Rotation
description: Problem Description and Solution for Determine Whether Matrix Can Be Obtained By Rotation
sidebar_label: 1886. Determine Whether Matrix Can Be Obtained By Rotation
sidebar_position: 1886
---

# [1886. Determine Whether Matrix Can Be Obtained By Rotation](https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/)

```py title=determine-whether-matrix-can-be-obtained-by-rotation.py
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        rows, cols = len(mat), len(mat[0])
        
        def rotate(M):
            M = list(reversed(M))
            
            for i in range(rows):
                for j in range(i + 1, cols):
                    M[i][j], M[j][i] = M[j][i], M[i][j]
            
            return M
        
        for _ in range(4):
            mat = rotate(mat)
            if mat == target: return True
            
        return mat == target
```


