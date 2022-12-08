---
id: optimal-partition-of-string
title: Optimal Partition of String
description: Problem Description and Solution for Optimal Partition of String
sidebar_label: 2405. Optimal Partition of String
sidebar_position: 2405
---

# [2405. Optimal Partition of String](https://leetcode.com/problems/optimal-partition-of-string/)

```py title=optimal-partition-of-string.py
class Solution:
    def partitionString(self, s: str) -> int:
        n = len(s)
        res = 1
        seen = set()
        
        for j, x in enumerate(s):
            if x in seen:
                seen.clear()
                res += 1
                
            seen.add(x)
        
        return res
```


