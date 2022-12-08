---
id: sum-of-numbers-with-units-digit-k
title: Sum of Numbers With Units Digit K
description: Problem Description and Solution for Sum of Numbers With Units Digit K
sidebar_label: 2310. Sum of Numbers With Units Digit K
sidebar_position: 2310
---

# [2310. Sum of Numbers With Units Digit K](https://leetcode.com/problems/sum-of-numbers-with-units-digit-k/)

```py title=sum-of-numbers-with-units-digit-k.py
class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0: return 0
        
        for i in range(1, 11):
            if (i * k) % 10 == num % 10 and i * k <= num:
                return i
        
        return -1
```


