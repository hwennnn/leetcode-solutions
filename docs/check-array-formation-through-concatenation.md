---
id: check-array-formation-through-concatenation
title: Check Array Formation Through Concatenation
description: Problem Description and Solution for Check Array Formation Through Concatenation
sidebar_label: 1640. Check Array Formation Through Concatenation
sidebar_position: 1640
---

# [1640. Check Array Formation Through Concatenation](https://leetcode.com/problems/check-array-formation-through-concatenation/)

```py title=check-array-formation-through-concatenation.py
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        mp = {x[0]:x for x in pieces}
        
        res = []
        
        for num in arr:
            res += mp.get(num, [])
        
        return arr == res
```


