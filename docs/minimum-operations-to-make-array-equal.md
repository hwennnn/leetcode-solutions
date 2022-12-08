---
id: minimum-operations-to-make-array-equal
title: Minimum Operations to Make Array Equal
description: Problem Description and Solution for Minimum Operations to Make Array Equal
sidebar_label: 1551. Minimum Operations to Make Array Equal
sidebar_position: 1551
---

# [1551. Minimum Operations to Make Array Equal](https://leetcode.com/problems/minimum-operations-to-make-array-equal/)

```py title=minimum-operations-to-make-array-equal.py
class Solution:
    def minOperations(self, n: int) -> int:
        arr = [(2 * i) + 1 for i in range(n)]
        t = sum(arr) // n
        
        res = 0
        
        for num in arr:
            res += abs(t - num)
        
        return res // 2
```


