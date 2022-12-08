---
id: find-valid-matrix-given-row-and-column-sums
title: Find Valid Matrix Given Row and Column Sums
description: Problem Description and Solution for Find Valid Matrix Given Row and Column Sums
sidebar_label: 1605. Find Valid Matrix Given Row and Column Sums
sidebar_position: 1605
---

# [1605. Find Valid Matrix Given Row and Column Sums](https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/)

```py title=find-valid-matrix-given-row-and-column-sums.py
class Solution:
    def restoreMatrix(self, rs: List[int], cs: List[int]) -> List[List[int]]:
        r = len(rs)
        c = len(cs)
        
        lst = [[0]*c for _ in range(r)]
        
        for i in range(r):
            for j in range(c):
                
                cur = min(rs[i], cs[j])
                
                lst[i][j] = cur
                rs[i] -= cur
                cs[j] -= cur

        return lst
                
```


