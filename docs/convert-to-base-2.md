---
id: convert-to-base-2
title: Convert to Base -2
description: Problem Description and Solution for Convert to Base -2
sidebar_label: 1017. Convert to Base -2
sidebar_position: 1017
---

# [1017. Convert to Base -2](https://leetcode.com/problems/convert-to-base-2/)

```py title=convert-to-base-2.py
class Solution:
    def baseNeg2(self, n: int) -> str:
        res = []

        while n != 0:
            res.append(n & 1)
            n = -(n >> 1)
        
        return "".join(map(str, res[::-1] or [0]))
```


