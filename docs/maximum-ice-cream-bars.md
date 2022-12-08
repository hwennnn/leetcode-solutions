---
id: maximum-ice-cream-bars
title: Maximum Ice Cream Bars
description: Problem Description and Solution for Maximum Ice Cream Bars
sidebar_label: 1833. Maximum Ice Cream Bars
sidebar_position: 1833
---

# [1833. Maximum Ice Cream Bars](https://leetcode.com/problems/maximum-ice-cream-bars/)

```py title=maximum-ice-cream-bars.py
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        
        res = 0
        
        for c in costs:
            if coins >= c:
                coins -= c
                res += 1
            else:
                break
        
        return res
```


