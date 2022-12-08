---
id: maximum-consecutive-floors-without-special-floors
title: Maximum Consecutive Floors Without Special Floors
description: Problem Description and Solution for Maximum Consecutive Floors Without Special Floors
sidebar_label: 2274. Maximum Consecutive Floors Without Special Floors
sidebar_position: 2274
---

# [2274. Maximum Consecutive Floors Without Special Floors](https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/)

```py title=maximum-consecutive-floors-without-special-floors.py
class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        res = max(special[0] - bottom, top - special[-1])
        last = special[0] + 1
        
        for x in special[1:]:
            res = max(res, x - last)
            last = x + 1
        
        return res
```


