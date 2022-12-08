---
id: power-of-four
title: Power of Four
description: Problem Description and Solution for Power of Four
sidebar_label: 342. Power of Four
sidebar_position: 342
---

# [342. Power of Four](https://leetcode.com/problems/power-of-four/)

```py title=power-of-four.py
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n>=1 and not log(n,4)%1
        
```


