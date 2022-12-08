---
id: can-make-arithmetic-progression-from-sequence
title: Can Make Arithmetic Progression From Sequence
description: Problem Description and Solution for Can Make Arithmetic Progression From Sequence
sidebar_label: 1502. Can Make Arithmetic Progression From Sequence
sidebar_position: 1502
---

# [1502. Can Make Arithmetic Progression From Sequence](https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/)

```py title=can-make-arithmetic-progression-from-sequence.py
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n = len(arr)
        arr.sort()
        diff = arr[1] - arr[0]
        
        for i in range(2, n):
            d = arr[i] - arr[i - 1]
            if d != diff: return False
        
        return True
```


