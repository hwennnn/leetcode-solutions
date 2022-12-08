---
id: plates-between-candles
title: Plates Between Candles
description: Problem Description and Solution for Plates Between Candles
sidebar_label: 2055. Plates Between Candles
sidebar_position: 2055
---

# [2055. Plates Between Candles](https://leetcode.com/problems/plates-between-candles/)

```py title=plates-between-candles.py
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        A = [i for i, x in enumerate(s) if x == '|']
        res = []
        
        for start, end in queries:
            i = bisect.bisect_left(A, start)
            j = bisect.bisect(A, end) - 1
            res.append(A[j] - A[i] - (j - i) if i < j else 0)
        
        return res
```


