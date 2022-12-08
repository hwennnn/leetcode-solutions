---
id: subtract-the-product-and-sum-of-digits-of-an-integer
title: Subtract the Product and Sum of Digits of an Integer
description: Problem Description and Solution for Subtract the Product and Sum of Digits of an Integer
sidebar_label: 1281. Subtract the Product and Sum of Digits of an Integer
sidebar_position: 1281
---

# [1281. Subtract the Product and Sum of Digits of an Integer](https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/)

```py title=subtract-the-product-and-sum-of-digits-of-an-integer.py
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p = 1
        c = 0
        
        for i,x in enumerate(str(n)):
            p *= int(x)
            c += int(x)
        
        return p - c
```


