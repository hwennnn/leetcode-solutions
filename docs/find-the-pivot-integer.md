---
id: find-the-pivot-integer
title: Find the Pivot Integer
description: Problem Description and Solution for Find the Pivot Integer
sidebar_label: 2485. Find the Pivot Integer
sidebar_position: 2485
---

# [2485. Find the Pivot Integer](https://leetcode.com/problems/find-the-pivot-integer/)

```py title=find-the-pivot-integer.py
class Solution:
    def pivotInteger(self, n: int) -> int:
        prefix = [0]
        for x in range(1, n + 1):
            prefix.append(prefix[-1] + x)
        
        for i in range(1, n + 1):
            if prefix[i - 1] == prefix[-1] - prefix[i]:
                return i
        
        return -1
```


