---
id: number-of-1-bits
title: Number of 1 Bits
description: Problem Description and Solution for Number of 1 Bits
sidebar_label: 191. Number of 1 Bits
sidebar_position: 191
---

# [191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)

```py title=number-of-1-bits.py
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        
        while n > 0:
            if n & 1:
                res += 1
            n >>= 1
        
        return res
```


