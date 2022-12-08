---
id: simplified-fractions
title: Simplified Fractions
description: Problem Description and Solution for Simplified Fractions
sidebar_label: 1447. Simplified Fractions
sidebar_position: 1447
---

# [1447. Simplified Fractions](https://leetcode.com/problems/simplified-fractions/)

```py title=simplified-fractions.py
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        for i in range(2, n + 1):
            for j in range(1, i):
                if math.gcd(i, j) == 1:
                    res.append(str(j) + '/' + str(i))
        return res
```


