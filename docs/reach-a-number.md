---
id: reach-a-number
title: Reach a Number
description: Problem Description and Solution for Reach a Number
sidebar_label: 754. Reach a Number
sidebar_position: 754
---

# [754. Reach a Number](https://leetcode.com/problems/reach-a-number/)

```py title=reach-a-number.py
class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        step = c = 0
        
        while c < target:
            step += 1
            c += step
        
        while (c - target) % 2 != 0:
            step += 1
            c += step
        
        return step
```


