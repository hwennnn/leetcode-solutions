---
id: minimum-time-to-make-rope-colorful
title: Minimum Time to Make Rope Colorful
description: Problem Description and Solution for Minimum Time to Make Rope Colorful
sidebar_label: 1578. Minimum Time to Make Rope Colorful
sidebar_position: 1578
---

# [1578. Minimum Time to Make Rope Colorful](https://leetcode.com/problems/minimum-time-to-make-rope-colorful/)

```py title=minimum-time-to-make-rope-colorful.py
class Solution:
    def minCost(self, S: str, cost: List[int]) -> int:
        
        res = m = s = 0
        
        for i, x in enumerate(S):
            if i > 0 and S[i] != S[i-1]:
                res += s - m
                s = m = 0
            
            s += cost[i]
            m = max(m, cost[i])
        
        res += s - m
        return res
            
```


