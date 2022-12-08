---
id: maximum-bags-with-full-capacity-of-rocks
title: Maximum Bags With Full Capacity of Rocks
description: Problem Description and Solution for Maximum Bags With Full Capacity of Rocks
sidebar_label: 2279. Maximum Bags With Full Capacity of Rocks
sidebar_position: 2279
---

# [2279. Maximum Bags With Full Capacity of Rocks](https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/)

```py title=maximum-bags-with-full-capacity-of-rocks.py
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], extra: int) -> int:
        res = 0
        A = []
        
        for cap, rock in zip(capacity, rocks):
            if cap == rock:
                res += 1
                continue
            
            A.append(cap - rock)
        A.sort()
        
        for x in A:
            if extra >= x:
                res += 1
                extra -= x
            else:
                break
        
        return res
```


