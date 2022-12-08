---
id: n-queens-ii
title: N-Queens II
description: Problem Description and Solution for N-Queens II
sidebar_label: 52. N-Queens II
sidebar_position: 52
---

# [52. N-Queens II](https://leetcode.com/problems/n-queens-ii/)

```py title=n-queens-ii.py
class Solution:
    def totalNQueens(self, n: int) -> int:
        cols, diag1, diag2 = set(), set(), set()
        
        def go(row):
            if row == n: return 1
            
            res = 0
            
            for col in range(n):
                if col not in cols and row - col not in diag1 and row + col not in diag2:
                    cols.add(col)
                    diag1.add(row - col)
                    diag2.add(row + col)
                    res += go(row + 1)
                    cols.remove(col)
                    diag1.remove(row - col)
                    diag2.remove(row + col)
            
            return res
        
        return go(0)
```


