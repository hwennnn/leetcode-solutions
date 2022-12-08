---
id: reverse-bits
title: Reverse Bits
description: Problem Description and Solution for Reverse Bits
sidebar_label: 190. Reverse Bits
sidebar_position: 190
---

# [190. Reverse Bits](https://leetcode.com/problems/reverse-bits/)

```py title=reverse-bits.py
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        
        for i in range(32):
            res = (res << 1) + (n & 1)
            n >>= 1
        
        return res
```


