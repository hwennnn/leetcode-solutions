---
id: number-of-common-factors
title: Number of Common Factors
description: Problem Description and Solution for Number of Common Factors
sidebar_label: 2427. Number of Common Factors
sidebar_position: 2427
---

# [2427. Number of Common Factors](https://leetcode.com/problems/number-of-common-factors/)

```py title=number-of-common-factors.py
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        res = 0
        
        for x in range(1, min(a, b) + 1):
            if a % x == 0 and b % x == 0:
                res += 1
        
        return res
```


