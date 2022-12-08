---
id: power-of-two
title: Power of Two
description: Problem Description and Solution for Power of Two
sidebar_label: 231. Power of Two
sidebar_position: 231
---

# [231. Power of Two](https://leetcode.com/problems/power-of-two/)

```py title=power-of-two.py
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        while n >= 2:
            # print(n)
            n /= 2
        # print(n)
        return n == 1
```


