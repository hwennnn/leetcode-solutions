---
id: power-of-three
title: Power of Three
description: Problem Description and Solution for Power of Three
sidebar_label: 326. Power of Three
sidebar_position: 326
---

# [326. Power of Three](https://leetcode.com/problems/power-of-three/)

```py title=power-of-three.py
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0: return False
        
        if n == 1: return True
        
        if n % 3 != 0: return False
        
        return self.isPowerOfThree(n // 3)
```


