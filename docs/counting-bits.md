---
id: counting-bits
title: Counting Bits
description: Problem Description and Solution for Counting Bits
sidebar_label: 338. Counting Bits
sidebar_position: 338
---

# [338. Counting Bits](https://leetcode.com/problems/counting-bits/)

```py title=counting-bits.py
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        
        for i in range(n + 1):
            res.append(i.bit_count())
        
        return res
```


