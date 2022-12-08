---
id: teemo-attacking
title: Teemo Attacking
description: Problem Description and Solution for Teemo Attacking
sidebar_label: 495. Teemo Attacking
sidebar_position: 495
---

# [495. Teemo Attacking](https://leetcode.com/problems/teemo-attacking/)

```py title=teemo-attacking.py
class Solution(object):
    def findPoisonedDuration(self, ts, d):
        n = len(ts)
        if n == 0: return 0
        
        res = d
        
        for i in range(1, n):
            if ts[i] - ts[i-1] > d:
                res += d
            else:
                res += ts[i] - ts[i-1]
        
        return res
        
```


