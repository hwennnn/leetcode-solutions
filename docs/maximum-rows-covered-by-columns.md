---
id: maximum-rows-covered-by-columns
title: Maximum Rows Covered by Columns
description: Problem Description and Solution for Maximum Rows Covered by Columns
sidebar_label: 2397. Maximum Rows Covered by Columns
sidebar_position: 2397
---

# [2397. Maximum Rows Covered by Columns](https://leetcode.com/problems/maximum-rows-covered-by-columns/)

```py title=maximum-rows-covered-by-columns.py
class Solution:
    def maximumRows(self, mat: List[List[int]], k: int) -> int:
        rows, cols = len(mat), len(mat[0])
        res = 0
        
        A = list(range(cols))

        for mask in range(1, 1 << cols):
            if mask.bit_count() != k: continue
            
            filled = 0
            
            for row in mat:
                ones = row.count(1)
                curr = 0
                
                for j in range(cols):
                    if mask & (1 << j) > 0 and row[j] == 1:
                        curr += 1
                
                if curr == ones:
                    filled += 1
                
            res = max(res, filled)
            
        return res
```


