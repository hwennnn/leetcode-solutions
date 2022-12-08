---
id: ugly-number
title: Ugly Number
description: Problem Description and Solution for Ugly Number
sidebar_label: 263. Ugly Number
sidebar_position: 263
---

# [263. Ugly Number](https://leetcode.com/problems/ugly-number/)

```py title=ugly-number.py
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0: return False

        while n % 5 == 0: n //= 5
        while n % 3 == 0: n //= 3
        while n % 2 == 0: n //= 2

        return n == 1
```


