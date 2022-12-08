---
id: sum-of-digits-in-base-k
title: Sum of Digits in Base K
description: Problem Description and Solution for Sum of Digits in Base K
sidebar_label: 1837. Sum of Digits in Base K
sidebar_position: 1837
---

# [1837. Sum of Digits in Base K](https://leetcode.com/problems/sum-of-digits-in-base-k/)

```py title=sum-of-digits-in-base-k.py
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        res = 0
        
        while n > 0:
            res += n % k
            n //= k
        
        return res
        
```


