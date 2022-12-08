---
id: swap-adjacent-in-lr-string
title: Swap Adjacent in LR String
description: Problem Description and Solution for Swap Adjacent in LR String
sidebar_label: 777. Swap Adjacent in LR String
sidebar_position: 777
---

# [777. Swap Adjacent in LR String](https://leetcode.com/problems/swap-adjacent-in-lr-string/)

```py title=swap-adjacent-in-lr-string.py
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if start == end: return True
        
        A = [(i, x) for i, x in enumerate(start) if x != "X"]
        B = [(i, x) for i, x in enumerate(end) if x != "X"]
        
        if len(A) != len(B): return False
        
        for (i, a), (j, b) in zip(A, B):
            if a != b: return False
            
            if a == "L":
                if i < j: return False
            else:
                if i > j: return False
        
        return True
```


