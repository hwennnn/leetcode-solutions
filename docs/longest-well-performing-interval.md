---
id: longest-well-performing-interval
title: Longest Well-Performing Interval
description: Problem Description and Solution for Longest Well-Performing Interval
sidebar_label: 1124. Longest Well-Performing Interval
sidebar_position: 1124
---

# [1124. Longest Well-Performing Interval](https://leetcode.com/problems/longest-well-performing-interval/)

```py title=longest-well-performing-interval.py
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        seen = {}
        res = v = 0
        
        for i, h in enumerate(hours):
            v = v + 1 if h > 8 else v - 1
                        
            if v > 0:
                res = i + 1
                
            seen.setdefault(v, i)

            if v - 1 in seen:
                res = max(res, i - seen[v - 1])
        
        return res
```


