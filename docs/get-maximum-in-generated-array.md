---
id: get-maximum-in-generated-array
title: Get Maximum in Generated Array
description: Problem Description and Solution for Get Maximum in Generated Array
sidebar_label: 1646. Get Maximum in Generated Array
sidebar_position: 1646
---

# [1646. Get Maximum in Generated Array](https://leetcode.com/problems/get-maximum-in-generated-array/)

```py title=get-maximum-in-generated-array.py
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0: return 0
        if n <= 1: return 1
        res = [0] * (n+1)
        res[0] = 0
        res[1] = 1
        
        i = 1
        while 2*i <= n:
            res[2*i] = res[i]
            if (2 * i) + 1 <= n:
                res[(2 * i) + 1] = res[i] + res[i+1]
            i += 1
            
        return max(res)
```


