---
id: matrix-diagonal-sum
title: Matrix Diagonal Sum
description: Problem Description and Solution for Matrix Diagonal Sum
sidebar_label: 1572. Matrix Diagonal Sum
sidebar_position: 1572
---

# [1572. Matrix Diagonal Sum](https://leetcode.com/problems/matrix-diagonal-sum/)

```py title=matrix-diagonal-sum.py
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        res = 0
        
        for i in range(rows):
            res += mat[i][i] + mat[i][-i-1]
        
        if rows & 1:
            res -= mat[rows // 2][rows // 2]
                
        return res
```

```cpp title=matrix-diagonal-sum.cpp
class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        int res = 0;
        int N = mat.size();
        
        for (int i = 0, j = N-1; i < N; i++, j--){
            if (i == j){
                res += mat[i][i];
            }else{
                res += mat[i][j] + mat[i][i];
            }
        }
        
        return res;
    }
};
```


