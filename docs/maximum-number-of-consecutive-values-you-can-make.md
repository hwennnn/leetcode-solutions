---
id: maximum-number-of-consecutive-values-you-can-make
title: Maximum Number of Consecutive Values You Can Make
description: Problem Description and Solution for Maximum Number of Consecutive Values You Can Make
sidebar_label: 1798. Maximum Number of Consecutive Values You Can Make
sidebar_position: 1798
---

# [1798. Maximum Number of Consecutive Values You Can Make](https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/)

```py title=maximum-number-of-consecutive-values-you-can-make.py
class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        res = 1
        
        for v in sorted(coins):
            if v > res:
                return res
            res += v
        
        return res
```


