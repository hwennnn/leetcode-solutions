---
id: maximum-units-on-a-truck
title: Maximum Units on a Truck
description: Problem Description and Solution for Maximum Units on a Truck
sidebar_label: 1710. Maximum Units on a Truck
sidebar_position: 1710
---

# [1710. Maximum Units on a Truck](https://leetcode.com/problems/maximum-units-on-a-truck/)

```py title=maximum-units-on-a-truck.py
class Solution:
    def maximumUnits(self, A: List[List[int]], truckSize: int) -> int:
        A.sort(key = lambda x : (-x[1], -x[0]))
        res = 0
        
        for k, x in A:
            take = min(k, truckSize)
            truckSize -= take
            res += take * x
        
        return res
```


