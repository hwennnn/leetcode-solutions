---
id: minimum-non-zero-product-of-the-array-elements
title: Minimum Non-Zero Product of the Array Elements
description: Problem Description and Solution for Minimum Non-Zero Product of the Array Elements
sidebar_label: 1969. Minimum Non-Zero Product of the Array Elements
sidebar_position: 1969
---

# [1969. Minimum Non-Zero Product of the Array Elements](https://leetcode.com/problems/minimum-non-zero-product-of-the-array-elements/)

```py title=minimum-non-zero-product-of-the-array-elements.py
class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        M = 10 ** 9 + 7
        
        return (pow(2 ** p - 2, 2 ** (p - 1) - 1, M) * (2 ** p - 1)) % M
```


