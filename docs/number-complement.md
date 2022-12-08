---
id: number-complement
title: Number Complement
description: Problem Description and Solution for Number Complement
sidebar_label: 476. Number Complement
sidebar_position: 476
---

# [476. Number Complement](https://leetcode.com/problems/number-complement/)

```py title=number-complement.py
class Solution:
    def findComplement(self, num: int) -> int:

        return ((1 << num.bit_length()) - 1) ^ num
```


