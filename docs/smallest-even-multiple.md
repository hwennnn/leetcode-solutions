---
id: smallest-even-multiple
title: Smallest Even Multiple
description: Problem Description and Solution for Smallest Even Multiple
sidebar_label: 2413. Smallest Even Multiple
sidebar_position: 2413
---

# [2413. Smallest Even Multiple](https://leetcode.com/problems/smallest-even-multiple/)

```py title=smallest-even-multiple.py
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0: return n
        
        return n * 2
```


