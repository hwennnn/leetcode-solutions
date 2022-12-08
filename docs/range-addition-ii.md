---
id: range-addition-ii
title: Range Addition II
description: Problem Description and Solution for Range Addition II
sidebar_label: 598. Range Addition II
sidebar_position: 598
---

# [598. Range Addition II](https://leetcode.com/problems/range-addition-ii/)

```py title=range-addition-ii.py
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        rows, cols = m, n
        
        for r, c in ops:
            rows = min(rows, r)
            cols = min(cols, c)
        
        return rows * cols
```


