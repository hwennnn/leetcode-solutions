---
id: maximize-distance-to-closest-person
title: Maximize Distance to Closest Person
description: Problem Description and Solution for Maximize Distance to Closest Person
sidebar_label: 849. Maximize Distance to Closest Person
sidebar_position: 849
---

# [849. Maximize Distance to Closest Person](https://leetcode.com/problems/maximize-distance-to-closest-person/)

```py title=maximize-distance-to-closest-person.py
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        res, last = 0, -1
        
        for i, x in enumerate(seats):
            if x == 1:
                res = max(res, i if last == -1 else (i - last) // 2)
                last = i
        
        res = max(res, n - last - 1)
        
        return res
```


