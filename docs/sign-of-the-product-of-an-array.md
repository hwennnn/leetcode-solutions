---
id: sign-of-the-product-of-an-array
title: Sign of the Product of an Array
description: Problem Description and Solution for Sign of the Product of an Array
sidebar_label: 1822. Sign of the Product of an Array
sidebar_position: 1822
---

# [1822. Sign of the Product of an Array](https://leetcode.com/problems/sign-of-the-product-of-an-array/)

```py title=sign-of-the-product-of-an-array.py
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        x = 1
        
        for y in nums:
            x *= y
        
        return 1 if x > 0 else -1 if x < 0 else 0
```


