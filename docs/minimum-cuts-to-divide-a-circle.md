---
id: minimum-cuts-to-divide-a-circle
title: Minimum Cuts to Divide a Circle
description: Problem Description and Solution for Minimum Cuts to Divide a Circle
sidebar_label: 2481. Minimum Cuts to Divide a Circle
sidebar_position: 2481
---

# [2481. Minimum Cuts to Divide a Circle](https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/)

```py title=minimum-cuts-to-divide-a-circle.py
class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n == 1: return 0
        if n % 2 == 0: return n // 2
        
        return n
```


