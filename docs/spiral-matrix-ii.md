---
id: spiral-matrix-ii
title: Spiral Matrix II
description: Problem Description and Solution for Spiral Matrix II
sidebar_label: 59. Spiral Matrix II
sidebar_position: 59
---

# [59. Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/)

```py title=spiral-matrix-ii.py
class Solution:
    def generateMatrix(self, n):
        res, lo = [[n*n]], n*n 
        while lo > 1:
            lo, hi = lo - len(res), lo
            #print('res:', res)
            res = [[i for i in range(lo, hi)]] + [list(j) for j in zip(*res[::-1])]
        return res
```


