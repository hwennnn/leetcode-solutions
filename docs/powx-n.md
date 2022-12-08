---
id: powx-n
title: Pow(x, n)
description: Problem Description and Solution for Pow(x, n)
sidebar_label: 50. Pow(x, n)
sidebar_position: 50
---

# [50. Pow(x, n)](https://leetcode.com/problems/powx-n/)

```py title=powx-n.py
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        
        if n < 0:
            n = -n
            x = 1 / x
        
        return self.myPow(x * x, n // 2) if n % 2 == 0 else x * self.myPow(x * x, n // 2)
```


