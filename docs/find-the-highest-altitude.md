---
id: find-the-highest-altitude
title: Find the Highest Altitude
description: Problem Description and Solution for Find the Highest Altitude
sidebar_label: 1732. Find the Highest Altitude
sidebar_position: 1732
---

# [1732. Find the Highest Altitude](https://leetcode.com/problems/find-the-highest-altitude/)

```py title=find-the-highest-altitude.py
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = [0]
        for g in gain:
            res.append(res[-1]+g)
        
        return max(res)
        
```


