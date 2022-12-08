---
id: add-minimum-number-of-rungs
title: Add Minimum Number of Rungs
description: Problem Description and Solution for Add Minimum Number of Rungs
sidebar_label: 1936. Add Minimum Number of Rungs
sidebar_position: 1936
---

# [1936. Add Minimum Number of Rungs](https://leetcode.com/problems/add-minimum-number-of-rungs/)

```py title=add-minimum-number-of-rungs.py
class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        prev = res = 0
        
        for rung in rungs:
            res += (rung - prev - 1) // dist
            prev = rung
        
        return res
```


